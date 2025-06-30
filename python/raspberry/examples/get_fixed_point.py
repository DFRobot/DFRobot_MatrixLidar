# -*- coding: utf-8 -*-
"""
@file get_fixed_point.py
@brief This is a demo to retrieve the distance to a specific point. By configuring and running, you can obtain data for the specified coordinates.
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
	data = tof.get_fixed_point_data(1,0)
	print("data:", data)
	time.sleep(1)
  
    
if __name__ == "__main__":
  setup()
  while True:
    loop()