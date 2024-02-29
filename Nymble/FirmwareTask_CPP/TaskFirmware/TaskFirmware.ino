
//This is the Firmware code for Nymble Task https://nymblelabs.notion.site/Firmware-Task-5177116a6cb94643871d8cf39c1f345f
// This particular code is the cpp based version of the fw where the CPP file contains all the required functions.


#include "TaskFirmware.h"
#include "EEPROM.h"
void setup() {
  Serial.begin(2400);
  if (!CheckEEPROM()) {
    Serial.println("Failed to initialise EEPROM");
    Serial.println("Restarting...");
    delay(1000);
    ESP.restart();
  }
}

int address = 0;
void loop() {
  if (Serial.available()) {

    SerialtoEEPROM(Serial.readString());

    Serial.println(EEPROMtoSerial());
  }
}
