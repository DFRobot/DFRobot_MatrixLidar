# DFRobot_MatrixLidar
- [English Version](./README.md)

这是一个获取TOF原始数据和避障建议的用户库。

![](./resources/images/SEN0628.png)

## 产品链接(https://www.dfrobot.com.cn)

    SKU：SEN0628

## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性y)
* [历史](#历史)
* [创作者](#创作者)

## 概述
  一个获取TOF原始数据和避障建议的用户库。

## 库安装

使用此库前，请首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开examples文件夹并在该文件夹中运行演示。

## 方法

```C++
    /**
     * @fn begin
     * @brief 初始化传感器
     * @return NULL
     */
    uint8_t begin(void);

    /**
     * @fn setRangingMode
     * @brief 获取全部数据的配置
     * @param matrix 配置传感器采样矩阵
     * @return 返回配置状态
     * @retval 0 成功
     * @retval 1 失败
     */
     uint8_t setRangingMode(eMatrix_t matrix);

    /**
     * @fn getAllData
     * @brief 获取全部数据
     * @param buf 存储数据
     */
    uint8_t getAllData(void *buf);

    /**
     * @fn getFixedPointData
     * @brief 获取指定点的数据
     * @param x 坐标x
     * @param y 坐标y
     * @return 返回获取的数据
     */
    uint16_t getFixedPointData(uint8_t x, uint8_t y);

```

## 兼容性

| 主板          | 通过 | 未通过 | 未测试 | 备注 |
| ------------- | :--: | :----: | :----: | ---- |
| Arduino uno   |  √   |        |        |      |
| Mega2560      |  √   |        |        |      |
| Leonardo      |  √   |        |        |      |
| ESP32         |  √   |        |        |      |
| micro:bit     |  √   |        |        |      |
| FireBeetle M0 |  √   |        |        |      |


## 历史

- 日期 2025-04-02 
- 版本 V1.0.0


## 创作者

Written by tangjie(jie.tang@dfrobot.com), 2024. (Welcome to our [website](https://www.dfrobot.com/))

