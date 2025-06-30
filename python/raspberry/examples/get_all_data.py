# -*- coding: utf-8 -*-
"""
@file get_all_data.py
@brief This is a demo to retrieve all matrix data. Running this code will print the matrix data.
@copyright  Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
@license     The MIT License (MIT)
@author [tangjie](jie.tang@dfrobot.com)
@version  V1.0
@date  2025-04-03
@url https://github.com/DFRobot/DFRobot_matrixLidarDistanceSensor
"""

from __future__ import print_function
import sys
import os
sys.path.append("../")
import time

from python.raspberry.DFRobot_matrixLidar import *

ADDRESS = 0x33

# I2C mode
tof = DFRobot_matrixLidar_i2c(ADDRESS)

#uart mode
#tof = DFRobot_matrixLidar_uart()

def setup():
  while tof.begin() != 0:
    print("begin error!!!!")
    time.sleep(1)
  while tof.set_Ranging_Mode(8) != 0:
    print("init error")
    time.sleep(1)
    

def loop():
  data = tof.get_all_data()
  for index in range(0, len(data), 2):
    high_byte = data[index + 1]
    low_byte = data[index ]
    combined_value = (high_byte << 8) | low_byte 
    print(combined_value, end=' ')
    if (index // 2 + 1) % 4 == 0:
      print() 
  print("-------------------")
  time.sleep(1)
  
    
if __name__ == "__main__":
  setup()
  while True:
    loop()