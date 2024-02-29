
#include"TaskFirmware.h"
#include "EEPROM.h"
bool CheckEEPROM() {
  bool EEPROMflag = true;
  if (!EEPROM.begin(1000)) {
    bool EEPROMflag = false;
    delay(1000);
  }
  return EEPROMflag;
}
void SerialtoEEPROM(String sentence) {
  int address = 0;

  EEPROM.writeString(address, sentence);
  // address += sentence.length() + 1;
  // See also the general purpose writeBytes() and readBytes() for BLOB in EEPROM library
  EEPROM.commit();
}
String EEPROMtoSerial() {
  return (EEPROM.readString(0));
}
