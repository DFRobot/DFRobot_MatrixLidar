/*!
 * @file get4_4Data.ino
 * @brief This is a demo for retrieving all TOF data. Running this demo will allow you to get all TOF data.
 * @copyright  Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT License (MIT)
 * @author [tangjie](jie.tang@dfrobot.com)
 * @version  V1.0
 * @date  2025-04-03
 * @url https://github.com/DFRobot/DFRobot_MatrixLidar
 */

 #include "DFRobot_MatrixLidar.h"

 DFRobot_MatrixLidar_I2C tof(0x33);
 uint16_t buf[16];
 
 void setup(void){
   Serial.begin(115200);
   while(tof.begin() != 0){
     Serial.println("begin error !!!!!");
   }
   Serial.println("begin success");
   //config matrix mode
   while(tof.setRangingMode(eMatrix_4x4) != 0){
     Serial.println("init error !!!!!");
     delay(1000);
   }
   Serial.println("init success");
 }
 
 void loop(void){
   tof.getAllData(buf);
   for(uint8_t i = 0; i < 4; i++){
     Serial.print("Y");
     Serial.print(i);
     Serial.print(": ");
     for(uint8_t j = 0; j < 4; j++){
       Serial.print(buf[i * 4 + j]);
       Serial.print(",");
     }
     Serial.println("");
   }
   Serial.println("------------------------------");
   delay(100);
 }
 