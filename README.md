# Firmware Data Transmission Task
## Overview :
This project implements various firmware solutions for transmitting data between a PC and a microcontroller unit (MCU) via UART communication. The task involves sending a specific piece of text from the PC to the MCU, storing it in EEPROM memory, and then transmitting it back to the PC. Real-time data transmission speed is measured during both the sending and receiving processes.
## Features : 
- UART communication setup between PC and MCU.
- Data transmission from PC to MCU and vice versa.
- Data storage in MCU EEPROM.
- Real-time measurement of data transmission/reception speed.
- Multiple solutions provided, including:
  - .CPP and .H based INO file solution for Arduino.
  - PC code written in Python for communication with MCU.
  - PC Code with UI 

### MCU Used :
ESP32 Dev Kit: The ESP32 microcontroller development board is used for testing the firmware solutions.

## Implementation:

### MCU Firmware :
- .CPP and .H based INO file solution [(TaskFirmware)](Nymble/TaskFirmware): Utilizes separate .cpp and .h files for better code organization.
- PC Code: 
  - Written in Python [(Pc_Code_simple.py)](Nymble/Pc_Code_simple.py), establishes UART communication with the MCU, sends text data, and receives stored data.
  - [PC_Code_UI.py](Nymble/PC_Code_UI.py) is a UI solution for the PC side code.
### How to Use :
- Connect the  MCU to the PC via UART. Set BAUD RATE at 2400.
- Choose the desired MCU firmware solution and upload it to the microcontroller.
- Run the PC code on the computer. No major dependencies except for Pyserial which can be downloaded using `pip install Pyserial` in the terminal.
- Follow the instructions provided by the PC code to initiate data transmission.
- Monitor the console output for real-time data transmission/reception speed, number of bits transferred and received data.
