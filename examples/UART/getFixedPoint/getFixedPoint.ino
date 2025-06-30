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
#if defined(ARDUINO_AVR_UNO)||defined(ESP8266)
#include <SoftwareSerial.h>
#endif

#if defined(ARDUINO_AVR_UNO)||defined(ESP8266)
  SoftwareSerial mySerial(/*rx =*/4, /*tx =*/5);
  DFRobot_MatrixLidar_UART tof(&mySerial);
#else
  DFRobot_MatrixLidar_UART tof(&Serial1);
#endif
void setup(void){
  #if defined(ARDUINO_AVR_UNO)||defined(ESP8266)
    mySerial.begin(115200);
  #elif defined(ESP32)
    Serial1.begin(115200, SERIAL_8N1, /*rx =*/D3, /*tx =*/D2);
  #else
    Serial1.begin(115200);
  #endif
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
