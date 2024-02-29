

#include "EEPROM.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(2400);
  if (!EEPROM.begin(1000)) {
    Serial.println("Failed to initialise EEPROM");
    Serial.println("Restarting...");
    delay(1000);
    ESP.restart();
  }

}
int address = 0;
void loop() {
address = 0;

delay(1000);
if(Serial.available()){
  String sentence =Serial.readString();
  EEPROM.writeString(address, sentence);
  // address += sentence.length() + 1;
  // See also the general purpose writeBytes() and readBytes() for BLOB in EEPROM library
  EEPROM.commit();
  Serial.println(sentence);
  Serial.println(EEPROM.readString(address));

}

}
