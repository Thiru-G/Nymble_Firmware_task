#include "TaskFirmware.h"
#include "EEPROM.h"
void setup() {
  Serial.begin(115200);
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
