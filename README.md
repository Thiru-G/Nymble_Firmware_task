**Firmware Data Transmission Task**
Overview
This project implements various firmware solutions for transmitting data between a PC and a microcontroller unit (MCU) via UART communication. The task involves sending a specific piece of text from the PC to the MCU, storing it in EEPROM memory, and then transmitting it back to the PC. Real-time data transmission speed is measured during both the sending and receiving processes.
Features : 
UART communication setup between PC and MCU.
Data transmission from PC to MCU and vice versa.
Data storage in MCU EEPROM.
Real-time measurement of data transmission/reception speed.
Multiple firmware solutions provided, including:
Single .INO file solution for Arduino.
.CPP and .H based INO file solution for Arduino.
PC code written in Python for communication with MCU.
PC Code with UI 

MCU Used
ESP32 Dev Kit: The ESP32 microcontroller development board is used for testing the firmware solutions.
Implementation

MCU Firmware:
Single .INO file solution: Contains all firmware code/function in a single Arduino sketch file.
.CPP and .H based INO file solution: Utilizes separate .cpp and .h files for better code organization.
PC Code: 
Written in Python, establishes UART communication with the MCU, sends text data, and receives stored data.
PCUI is a UI solution for the PC side code.
How to Use
Connect the  MCU to the PC via UART. Set BAUD RATE at 2400
Choose the desired MCU firmware solution and upload it to the microcontroller.
Run the PC code on the computer. No major dependencies only Pyserial is required (Can be downloaded using "pip install Pyserial" in terminal)
Follow the instructions provided by the PC code to initiate data transmission.
Monitor the console output for real-time data transmission speed and received data.
