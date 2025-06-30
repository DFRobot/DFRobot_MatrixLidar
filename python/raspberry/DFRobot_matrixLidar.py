# -*- coding: utf-8 -*-
'''!
  @file        DFRobot_matrixLidar.py
  @brief       This is the implementation file for DFRobot_matrixLidar
  @copyright   Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      TangJie(jie.tang@dfrobot.com)
  @version     V1.0
  @date        2025-04-03
  @url         https://github.com/DFRobot/DFRobot_MatrixLidar
'''

import serial
import time
import smbus

ELEFT = 0
EMIDDLE = 1
ERIGHT = 2


class DFRobot_matrixLidar:
     
	CMD_SETMODE = 1
	CMD_ALLData  = 2
	CMD_FIXED_POINT  = 3
	CMD_LINE = 4
	CMD_LIST = 5
	CMD_AVOID_OBSTACLE = 6
	CMD_CONFIG_AVOID = 7
	CMD_OBSTACLE_DISTANCE = 8
	DEBUG_TIMEOUT_MS  =  8
	IIC_MAX_TRANSFER         =   32    #Maximum transferred data via I2C
	I2C_ACHE_MAX_LEN         =   32
	CMD_END         =    CMD_OBSTACLE_DISTANCE
	ERR_CODE_NONE           =    0x00 #Normal communication 
	ERR_CODE_CMD_INVAILED    =   0x01 #Invalid command
	ERR_CODE_RES_PKT         =   0x02 #Response packet error
	ERR_CODE_M_NO_SPACE      =   0x03 #Insufficient memory of I2C controller(master)
	ERR_CODE_RES_TIMEOUT     =   0x04 # Response packet reception timeout
	ERR_CODE_CMD_PKT         =   0x05 #Invalid command packet or unmatched command
	ERR_CODE_SLAVE_BREAK      =  0x06 #Peripheral(slave) fault
	ERR_CODE_ARGS             =  0x07 # Set wrong parameter
	ERR_CODE_SKU              =  0x08 # The SKU is an invalid SKU, or unsupported by SCI Acquisition Module
	ERR_CODE_S_NO_SPACE       =  0x09 # Insufficient memory of I2C peripheral(slave)
	ERR_CODE_I2C_ADRESS      =   0x0A # Invalid I2C address

	STATUS_SUCCESS   =   0x53  #Status of successful response   
	STATUS_FAILED     =  0x63  # Status of failed response 

	INDEX_ARGS_NUM_H = 0
	INDEX_ARGS_NUM_L = 1
	INDEX_CMD        = 2
     
	INDEX_RES_ERR    = 0
	INDEX_RES_STATUS = 1
	INDEX_RES_CMD    = 2
	INDEX_RES_LEN_L  = 3
	INDEX_RES_LEN_H  = 4
	INDEX_RES_DATA   = 5


	def __init__(self):
		self._dir = 0
		self._emergency_flaf = 0
		self._left = 0
		self._middle = 0
		self.right = 0
		self._list = list()
    
	def begin(self):
		"""
			@fn begin
			@brief Initialize the sensor
			@return Returns the initialization status
		"""
		return 0
  
	def set_Ranging_Mode(self, matrix):
		"""
			@fn set_Ranging_Mode
			@brief Retrieve the configuration for all data
			@param matrix Configure the sensor sampling matrix
			@return Returns the configuration status
			@retval 0 Success
			@retval 1 Failure
		"""
		length = 4
		pkt = [0] * (3 + length)
		pkt[self.INDEX_ARGS_NUM_H] = ((length + 1) >> 8) & 0xFF
		pkt[self.INDEX_ARGS_NUM_L] = (length+1) & 0xFF
		pkt[self.INDEX_CMD]        = self.CMD_SETMODE
		pkt[3]        = 0
		pkt[4]        = 0
		pkt[5]        = 0
		pkt[6]        = matrix
		self._send_packet(pkt)
		time.sleep(0.1)
		recv_pkt = self._recv_packet(self.CMD_SETMODE)
		if (len(recv_pkt) >= 5) and (recv_pkt[self.INDEX_RES_ERR] == self.ERR_CODE_NONE and recv_pkt[self.INDEX_RES_STATUS] == self.STATUS_SUCCESS):
			time.sleep(5)
			return 0
		return 1
      
	def get_all_data(self):
		'''!
      		@fn get_all_data
      		@brief Retrieves all data
      		@return Returns the retrieved data
    	'''
		length = 0
		pkt = [0] * (3 + length)
		pkt[self.INDEX_ARGS_NUM_H] = ((length + 1) >> 8) & 0xFF
		pkt[self.INDEX_ARGS_NUM_L] = (length+1) & 0xFF
		pkt[self.INDEX_CMD]        = self.CMD_ALLData
		self._send_packet(pkt)
		time.sleep(0.1)
		recv_pkt = self._recv_packet(self.CMD_ALLData)
		if (len(recv_pkt) >= 5) and (recv_pkt[self.INDEX_RES_ERR] == self.ERR_CODE_NONE and recv_pkt[self.INDEX_RES_STATUS] == self.STATUS_SUCCESS):
			length = recv_pkt[self.INDEX_RES_LEN_L] | (recv_pkt[self.INDEX_RES_LEN_H] << 8)
			if length:
				self._list = recv_pkt[self.INDEX_RES_DATA:]
				return self._list
		return self._list
    
	def get_fixed_point_data(self, x, y):
		'''!
			@fn get_fixed_point_data
      		@brief Retrieves data for a specific desk label
      		@param x X coordinate
      		@param y Y coordinate
      		@return Returns the retrieved data
    	'''
		rslt = -1
		length = 2
		pkt = [0] * (3 + length)
		pkt[self.INDEX_ARGS_NUM_H] = ((length + 1) >> 8) & 0xFF
		pkt[self.INDEX_ARGS_NUM_L] = (length+1) & 0xFF
		pkt[self.INDEX_CMD]        = self.CMD_FIXED_POINT
		pkt[3]        = x
		pkt[4]        = y
		self._send_packet(pkt)
		time.sleep(0.1)
		recv_pkt = self._recv_packet(self.CMD_FIXED_POINT)
		if (len(recv_pkt) >= 5) and (recv_pkt[self.INDEX_RES_ERR] == self.ERR_CODE_NONE and recv_pkt[self.INDEX_RES_STATUS] == self.STATUS_SUCCESS):
			length = recv_pkt[self.INDEX_RES_LEN_L] | (recv_pkt[self.INDEX_RES_LEN_H] << 8)
			if length:
				rslt = recv_pkt[self.INDEX_RES_DATA + 1] << 8 | recv_pkt[self.INDEX_RES_DATA ]
			return rslt
		return rslt
  
	def _recv_packet(self, cmd):
		'''!
			@brief Receive and parse the response data packet
			@param cmd Command to receive the packet
			@return Error code and response packet list
			@n      The zeroth element in the list: error code, only when the error code is ERR_CODE_NONE, there can be other elements
			@n      The first element in the list: response packet status code, 0x53-correct response packet 0x63-wrong response packet
			@n      The second element in the list: response packet command, which indicates the response packet belongs to which communication command
			@n      The third element in the list: low byte of the valid data length after the response packet
			@n      The fourth element in the list: high byte of the valid data length after the response packet
			@n      The 5th element or more in the list: valid data
		'''
		rslt = [0]
		t = time.time()
		while time.time() - t < self.DEBUG_TIMEOUT_MS:
			status = self._recv_data(1)
			if not status:
				continue
			status = status[0]
			#print(status)
			if status != 0xff:
				if status in [self.STATUS_SUCCESS, self.STATUS_FAILED]:
					command = self._recv_data(1)
					if not command:
						continue
					command = command[0]
					#print(command)
					if command != cmd:
						rslt[0] = self.ERR_CODE_RES_PKT
						return rslt
					lenL = self._recv_data(2)
					
					if not lenL or len(lenL) < 2:
						rslt[0] = self.ERR_CODE_RES_PKT
						print("Length read failed or too short.")  
						return rslt
					length = (lenL[1] << 2) | lenL[0]  
					if length > 128:
						return rslt 
					#print(length)
					rslt[0] = self.ERR_CODE_NONE
					rslt += [status, command, lenL[0], lenL[1]]
					if length:
						data = self._recv_data(length)
						rslt += data
					return rslt
			time.sleep(0.07)
		return [self.ERR_CODE_RES_TIMEOUT]



class DFRobot_matrixLidar_i2c(DFRobot_matrixLidar):
	def __init__(self,addr):
		'''!
		  @brief DFRobot_SCI_IIC Constructor
		  @param addr:  7-bit IIC address, support the following address settings
		  @n RP2040_SCI_ADDR_0X21      0x21 default I2C address
		  @n RP2040_SCI_ADDR_0X22      0x22
		  @n RP2040_SCI_ADDR_0X23      0x23
		'''
		self._addr = addr
		self._bus = smbus.SMBus(1)
		DFRobot_matrixLidar.__init__(self)
    
	def _recv_data(self, length):
		'''!
			@brief Read data
			@param length Number of bytes to be read
			@return The read data list
		'''
		rslt = [0]*length
		i = 0
		while i < length:
			try:
				rslt[i] = self._bus.read_byte(self._addr)
			except:
				rslt[i] = 0
			i += 1
		return rslt


	def _send_packet(self, pkt):
		'''!
	    	@brief Send data
	    	@param pkt List of data to be sent
	    	@return None
	  	'''
		register = 0x55  
		for data in pkt:
			try:
				self._bus.write_i2c_block_data(self._addr, register, pkt)
			except:
				pass

class DFRobot_matrixLidar_uart(DFRobot_matrixLidar):
  def __init__(self):
    '''!
      @brief DFRobot_SCI_IIC Constructor
      @param addr:  7-bit IIC address, support the following address settings
      @n RP2040_SCI_ADDR_0X21      0x21 default I2C address
      @n RP2040_SCI_ADDR_0X22      0x22
      @n RP2040_SCI_ADDR_0X23      0x23
    '''
    self.ser = serial.Serial("/dev/ttyAMA0", 115200, timeout=1)
    if self.ser.isOpen == False:
      self.ser.open()
    DFRobot_matrixLidar.__init__(self)
	
  def _send_packet(self, pkt):
    '''!
      @brief Send data
      @param pkt List of data to be sent
      @return None
    '''
    self.ser.write(b'\x55')
    self.ser.write(pkt)
    
  def _recv_data(self, length):
    '''!
      @brief Read data
      @param length Number of bytes to be read
      @return The read data list
    '''
    try:
        raw_data = self.ser.read(length)
        return [ord(byte) for byte in raw_data]
    except Exception as e:
        return [0] * length