import serial
import time

arduino = serial.Serial(port='/dev/cu.usbserial-0001',   baudrate=2400, timeout=.1)

def write_read(tosendstring):
    arduino.write(bytes(tosendstring,'utf-8'))
    return 
while True:
    inp = input("Enter the Data String: ")
    start_time_tx = time.time()
    write_read(inp)
    end_time_tx = time.time()
    transmission_time = end_time_tx - start_time_tx
    totbits=len(inp.encode('utf-8'))*8
    print('Total bits transferred : {0} '.format(totbits))
    print(f"Transmission Time: {transmission_time} seconds")
    print('Transmission Speed {0} bits/sec '.format(totbits/(transmission_time)))
    time.sleep(2)
    while arduino.inWaiting():
        start_time_rx = time.time()
        RecievedString= arduino.readline()
        end_time_rx = time.time()
        Reception_time = end_time_rx- start_time_rx
        totbitsrecieved=(len(RecievedString)-2) *8                        
        # Subtracting 2 Bytes for extra \r\n Characters recieved from MCU
        print('Total bits Recieved : {0} '.format(totbitsrecieved))
        print(f"Reception Time: {Reception_time} seconds")
        print('Reception ( MCU to PC) Speed {0} bits/sec '.format(totbitsrecieved/(Reception_time)))

        print('Recieved Data : {0}'.format(RecievedString.decode()))
