/*!
 * @file getFixedPoint.ino
 * @brief This is a demo to retrieve data from a specific point of the TOF sensor. Running this demo will obtain data from the specified point.
 * @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT License (MIT)
 * @author [tangjie](jie.tang@dfrobot.com)
 * @version  V1.0
 * @date  2025-04-03
 * @url https://github.com/DFRobot/DFRobot_MatrixLidar
 */

#include "DFRobot_MatrixLidar.h"
DFRobot_MatrixLidar_I2C tof(0x33);

void setup(void){
  Serial.begin(115200);

  while(tof.begin() != 0){
    Serial.println("begin error !!!!!");
  }
  Serial.println("begin success");
  //config matrix mode
  while(tof.setRangingMode(eMatrix_8X8) != 0){
    Serial.println("init error !!!!!");
    delay(1000);
  }
  Serial.println("init success");
}

void loop(void){

    uint16_t data = tof.getFixedPointData(1,0);
    Serial.print(data);
    Serial.println(" mm");
    delay(10);
}
