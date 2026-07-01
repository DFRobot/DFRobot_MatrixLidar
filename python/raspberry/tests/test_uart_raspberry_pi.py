"""Regression tests: the UART transport must be Python 3 compatible.

On Python 3 the previous code raised TypeError in two places, so the UART class
was unusable:
  - _send_packet did `self.ser.write(pkt)` with pkt a list[int]; pyserial needs
    a bytes-like object.
  - _recv_data did `[ord(byte) for byte in raw_data]`; iterating `bytes` already
    yields ints, so ord() raised, the except swallowed it, and every read
    returned zeros.

Host-only (mock serial); no sensor needed.

  python3 -m unittest python/raspberry/tests/test_uart_raspberry_pi.py
"""
import os
import sys
import types
import unittest

_serial = types.ModuleType("serial")


class _SerialException(Exception):
    pass


class FakeSerial:
    def __init__(self, *a, **k):
        self.is_open = True
        self.writes = []
        self._rx = bytearray()

    def write(self, b):
        # Reject a plain list the way pyserial does on Python 3, so the test
        # catches a regression to write(pkt).
        if not isinstance(b, (bytes, bytearray)):
            raise TypeError("write() needs a bytes-like object, not %s" % type(b).__name__)
        self.writes.append(bytes(b))
        return len(b)

    def read(self, n=1):
        out = bytes(self._rx[:n])
        del self._rx[:n]
        return out

    def reset_input_buffer(self):
        pass

    def open(self):
        pass


_serial.Serial = FakeSerial
_serial.SerialException = _SerialException
sys.modules["serial"] = _serial
sys.modules.setdefault("smbus", types.ModuleType("smbus"))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DFRobot_matrixLidar import DFRobot_matrixLidar_uart  # noqa: E402


class UartPython3Test(unittest.TestCase):
    def test_send_packet_writes_bytes_not_a_list(self):
        tof = DFRobot_matrixLidar_uart(port="/dev/serial0", baud=115200)
        tof.ser.writes.clear()
        tof._send_packet([0x00, 0x01, 0x02])  # would TypeError on Py3 before the fix
        sent = b"".join(tof.ser.writes)
        self.assertEqual(sent, b"\x55\x00\x01\x02")

    def test_recv_data_decodes_bytes_on_py3(self):
        tof = DFRobot_matrixLidar_uart(port="/dev/serial0", baud=115200)
        tof.ser._rx = bytearray(b"\x53\x02\x80\x00")
        self.assertEqual(tof._recv_data(4), [0x53, 0x02, 0x80, 0x00],
                         "Python 3 bytes must decode to ints (no ord(), no zeros)")


if __name__ == "__main__":
    unittest.main()
