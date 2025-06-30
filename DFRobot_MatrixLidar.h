/*!
 * @file DFRobot_MatrixLidar.h
 * @brief This is the method documentation file for DFRobot_MatrixLidar
 * @copyright   Copyright (c) 2024 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT License (MIT)
 * @author [TangJie](jie.tang@dfrobot.com)
 * @version  V1.0
 * @date  2025-04-03
 * @url https://github.com/DFRobot/DFRobot_MatrixLidar
 */
#ifndef _DFROBOT_MATRIXLIDAR_H_
#define _DFROBOT_MATRIXLIDAR_H_
#include "Arduino.h"
#include "Wire.h"

//#define ENABLE_DBG ///< Enable this macro to view the detailed execution process of the program.
#ifdef ENABLE_DBG
#define DBG(...) {Serial.print("[");Serial.print(__FUNCTION__); Serial.print("(): "); Serial.print(__LINE__); Serial.print(" ] "); Serial.println(__VA_ARGS__);}
#else
#define DBG(...)
#endif

/**
 * @brief matrix selection
 */
typedef enum{
  eMatrix_4x4  = 4,
  eMatrix_8X8  = 8, 
}eMatrix_t;

class DFRobot_MatrixLidar{
public:
    
  /**
   * @fn DFRobot_MatrixLidar
   * @brief Constructor for the TOF sensor
   * @param pWire Communication protocol initialization
   */
  DFRobot_MatrixLidar(void);
  
  /**
   * @fn begin
   * @brief Initializes the sensor
   * @return Returns the initialization status
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

protected:
  /**
   * @fn recvPacket
   * @brief Receive and parse the response data packet
   * 
   * @param cmd       Command to receive packet
   * @param errorCode Receive error code
   * @return Pointer array
   * @n      NULL    indicates receiving packet failed
   * @n      Non-NULL  response packet pointer
   */
  void* recvPacket(uint8_t cmd, uint8_t *errorCode);

  /**
   * @fn init
   * @brief Pure virtual function, interface init
   * 
   * @param freq     Communication frequency
   * @return Init status
   * @n       0    Init succeeded
   * @n      -1    Interface object is null pointer
   * @n      -2    Device does not exist
   */
  virtual int init(void) = 0;

  /**
   * @fn sendPacket
   * @brief I2C interface init
   * 
   * @param pkt    Set I2C communication frequency
   * @param length Set I2C communication frequency
   * @param stop   
   * @n     true   Stop
   * @n     false  Not stop
   */
  virtual void sendPacket(void *pkt, int length, bool stop) = 0;
  
  /**
   * @fn recvData
   * @brief I2C interface init
   * 
   * @param data    Store the received data cache
   * @param len     Byte number to be read
   * @return Actually read byte number    
   */
  virtual int recvData(void *data, int len) = 0;
    
private:
    uint32_t _timeout; ///< Time of receive timeout
    
};

class DFRobot_MatrixLidar_I2C:public DFRobot_MatrixLidar{
public:

  DFRobot_MatrixLidar_I2C(uint8_t addr = 0x33, TwoWire *pWire = &Wire);
  ~DFRobot_MatrixLidar_I2C();
private:
  TwoWire *_pWire;
  uint8_t _addr;
  int init(void);
  void sendPacket(void *pkt, int length, bool stop);
  int recvData(void *data, int len);

};

class DFRobot_MatrixLidar_UART:public DFRobot_MatrixLidar{
public:
  DFRobot_MatrixLidar_UART(Stream *s);
  ~DFRobot_MatrixLidar_UART();
private:
  uint8_t _state = 0;
  Stream *_s;
  int init(void);
  void sendPacket(void *pkt, int length, bool stop = true);
  int recvData(void *data, int len);
  
};

#endif
