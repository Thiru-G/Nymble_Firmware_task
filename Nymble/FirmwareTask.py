import serial
import time
# Below Function is used to establish a connection between MCU and PC Using Pyserial

Serialconn = serial.Serial(port='/dev/cu.usbserial-0001',baudrate=2400, timeout=.1)
# Below Function Writes data thru Serial Port : PC TO MCU
def PCtoMCU(tosendstring):
    Serialconn.write(bytes(tosendstring,'utf-8'))
    return 
def Serial_Tx_rx():
    inp = input("Enter the Data String: ")       #INPUT
    start_time_tx = time.time()                 #Marking Start of transmission
    PCtoMCU(inp)                                
    end_time_tx = time.time()                   #Marking END of transmission
    transmission_time = end_time_tx - start_time_tx     #Calc of transmission time
    totbits=len(inp.encode('utf-8'))*8                     # as given considering 1 character as a Byte, Total bytes * 8 is total bits
    print('Total bits transferred : {0} '.format(totbits))
    print(f"Transmission Time: {transmission_time} seconds")
    print('Transmission Speed {0} bits/sec '.format(totbits/(transmission_time)))
    time.sleep(2)                   #Timing buffer 
    while Serialconn.inWaiting():   # Checking serial inputs ,if available
        start_time_rx = time.time() #Marking Start of Reception
        RecievedString= Serialconn.readline()
        end_time_rx = time.time()   #Marking end of Reception
        Reception_time = end_time_rx- start_time_rx #Calc of Rec time
        totbitsrecieved=(len(RecievedString)-2) *8          # as given considering 1 character as a Byte, Total bytes * 8 is total bits                
        # Subtracting 2 Bytes for extra \r\n Characters recieved from MCU.EXample :  b' XYZ ABC \r\n'
        print('Total bits Recieved : {0} '.format(totbitsrecieved))
        print(f"Reception Time: {Reception_time} seconds")  
        print('Reception ( MCU to PC) Speed {0} bits/sec '.format(totbitsrecieved/(Reception_time)))
        print('Recieved Data : {0}'.format(RecievedString.decode()))

while True:
    Serial_Tx_rx()