# DFRobot_MatrixLidar

- [中文版](./README_CN.md)

This is a user library for retrieving TOF sensor raw data and providing obstacle avoidance suggestions.

![](./resources/images/SEN0628.png)

## Product Link (https://www.dfrobot.com)
    SKU:SEN0628

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary
This is a user library for retrieving TOF sensor raw data and providing obstacle avoidance suggestions.

## Installation

To use this library, download the library file first, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods

```C++
    /**
     * @fn begin
     * @brief Initializes the sensor
     * @return NULL
     */
    uint8_t begin(void);

     /**
     * @fn setRangingMode
     * @brief Configures the retrieval of all data
     * @param matrix Configuration matrix for sensor sampling
     * @return Returns the configuration status
     * @retval 0 Success
     * @retval 1 Failure
     */
    uint8_t setRangingMode(eMatrix_t matrix);


    /**
     * @fn getAllData
     * @brief Retrieves all data
     * @param buf Buffer to store the data
     */
    uint8_t getAllData(void *buf);

    /**
     * @fn getFixedPointData
     * @brief Retrieves data for a specific point
     * @param x X coordinate
     * @param y Y coordinate
     * @return Returns the retrieved data
     */
    uint16_t getFixedPointData(uint8_t x, uint8_t y);

```


## Compatibility

MCU                | Work Well | Work Wrong | Untested  | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Arduino uno |       √      |             |            | 
FireBeetle esp32 |       √      |             |            | 
FireBeetle esp8266 |       √      |             |            | 
FireBeetle m0 |       √      |             |            | 
Leonardo |       √      |             |            | 
Microbit |       √      |             |            | 
Arduino MEGA2560 | √ | | | 


## History

- data 2025-04-02
- version V1.0


## Credits

Written by tangjie(jie.tang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))
