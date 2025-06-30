# DFRobot_matrixLidarDistanceSensor
- [中文版](./README_CN.md)

This is a user library for retrieving TOF sensor raw data and providing obstacle avoidance suggestions.

![](./resources/images/SEN0628.png)

## Product link(https://www.dfrobot.com)

    SKU：SEN0628

## 目录

* [Overview](#Overview)
* [installation](#installation)
* [Methods](#Methods)
* [compatibility](#compatibility)
* [history](#history)
* [credits](#credits)

## Overview
This is a user library for retrieving TOF sensor raw data and providing obstacle avoidance suggestions.

## installation

Before using this library, first download the library files, paste them into the \Arduino\libraries directory, then open the examples folder and run the examples within that folder.

## Methods

```python
    def begin(self)
        '''!
            @fn begin
            @brief Initialize the sensor
            @return Returns the initialization status
        '''
  
    def set_Ranging_Mode(self, matrix)
        '''!
            @fn set_Ranging_Mode
            @brief Configure the retrieval of all data
            @param matrix Configuration matrix for sensor sampling
            @return Returns the configuration status
            @retval 0 Success
            @retval 1 Failure
        '''
  
      
    def get_all_data(self)
        '''!
            @fn get_all_data
            @brief Retrieve all data
            @return Returns the retrieved data
        '''
    
    def get_fixed_point_data(self, x, y)
        '''!
            @fn get_fixed_point_data
            @brief Retrieve data for a specific coordinate
            @param x X coordinate
            @param y Y coordinate
            @return Returns the retrieved data
        '''
  
```

## compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |     √     |            |          |         |
| RaspberryPi4 |           |            |     √    |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |           |            |    √     |         |
| Python3 |     √     |            |          |         |


## history

- 2024-09-9 - Version 1.0.0 released.

## credits

Written by TangJie(jie.tang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))





