import tkinter as tk
import tkinter.ttk as ttk
import sv_ttk
import serial
import time

def SerialConnection(e_text): 
    global Trspeed
    global recievedstring
    global Rxspeed
    arduino = serial.Serial(port='/dev/cu.usbserial-0001',   baudrate=2400, timeout=.1)
    def write_read(tosendstring):
        arduino.write(bytes(tosendstring,'utf-8'))
        print(tosendstring) 
        return 
 
    start_time = time.time()
    write_read(e_text)
    end_time = time.time()
    transmission_time = end_time - start_time
    totbits=len(e_text.encode('utf-8'))*8
    Trspeed = totbits/(transmission_time)
    print('Total bits transferred : {0} '.format(totbits))
    print(f"Transmission Time: {transmission_time} seconds")
    print('Transmission Speed {0} bits/sec '.format(totbits/(transmission_time)))
    time.sleep(2)
    print("SleepOver")
    while arduino.inWaiting():
        start_time_rx = time.time()
        RecievedString= arduino.readline()
        end_time_rx = time.time()
        recievedstring = RecievedString.decode()
        end_time_rx = time.time()
        Reception_time = end_time_rx - start_time_rx
        totbitsrecieved=(len(RecievedString)-2)*8                   
        # Subtracting 2 Bytes for extra \r\n Characters recieved from MCU
        print('Total bits Recieved : {0} '.format(totbitsrecieved))
        print(f"Reception Time: {Reception_time} seconds")
        print('Recieved Data : {0}'.format(RecievedString.decode()))
        print('Reception Speed {0} bits/sec '.format(totbitsrecieved/(Reception_time)))
        Rxspeed = (totbitsrecieved/(Reception_time))

class UIAPP:
    def __init__(self, master=None):
        # build ui
         
        global recievedstring
        global Trspeed
        global Rxspeed
        Trspeed = "Waiting For response"
        Rxspeed = "Waiting For response"
        recievedstring = "Waiting For response"
        def CallFunc_Ard():
            e_text=entry1.get()
            SerialConnection(e_text)
            label5.config(text = Trspeed)
            label6.config(text = recievedstring)
            label8.config(text = Rxspeed)

        frame1 = ttk.Frame(master)
        frame1.configure(height=500, width=500)
        labelTitle = tk.Label(frame1)
        labelTitle.configure(text='FIRMWARE TASK', font=('Helvetica', 30, 'bold') , height=10, width=50)
        labelTitle.place(anchor="center", height=30, relx=0.5, rely=0.06, x=0, y=0)
        Secondaryframe = ttk.Frame(frame1)
        Secondaryframe.configure(height=400, width=450)
        label2 = ttk.Label(Secondaryframe)
        label2.configure(text='Enter String')
        label2.place(anchor="center", relx=0.1, rely=0.1)
        BaudRateInfo = ttk.Label(Secondaryframe)
        BaudRateInfo.configure(text='BAUDRATE : 2400')
        BaudRateInfo.place(anchor="w", relx=0.01, rely=0.25)
        label4 = ttk.Label(Secondaryframe)
        label4.configure(text="Recieved String : ")
        label4.place(anchor="w", relx=0.01, rely=0.45)
        label6 = ttk.Label(Secondaryframe)
        label6.configure(text=recievedstring)
        label6.place(anchor="w", relx=0.4, rely=0.45)
        label4 = ttk.Label(Secondaryframe)
        label4.configure(text="TX. Speed (bits/Sec) : ")
        label4.place(anchor="w", relx=0.01, rely=0.35)
        label5 = ttk.Label(Secondaryframe)
        label5.configure(text=Trspeed)
        label5.place(anchor="w", relx=0.4, rely=0.35)
        label7 = ttk.Label(Secondaryframe)
        label7.configure(text="RX. Speed (bits/Sec) : ")
        label7.place(anchor="w", relx=0.01, rely=0.55)
        label8 = ttk.Label(Secondaryframe)
        label8.configure(text=Rxspeed)
        label8.place(anchor="w", relx=0.4, rely=0.55)
        button1 = ttk.Button(Secondaryframe)
        button1.configure(text='Send', command = CallFunc_Ard)
        button1.place(anchor="center", relx=0.5, rely=0.8, x=0, y=0)
        Secondaryframe.place(anchor="center", relx=.5, rely=.5, x=0, y=0)
        frame1.pack(side="top")
        frame1.pack(side="top")

        entry1 = ttk.Entry(Secondaryframe)
        entry1.place(anchor="center", relx=0.5, rely=0.1, x=0, y=0)
        Secondaryframe.place(anchor="center", relx=.5, rely=.5, x=0, y=0)
        button1 = ttk.Button(Secondaryframe)
        button1.configure(text='Submit', command = CallFunc_Ard)
        button1.place(anchor="center", relx=0.5, rely=0.8, x=0, y=0)
        # Main widget
        self.mainwindow = frame1
        sv_ttk.set_theme("dark")

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = UIAPP(root)
    app.run()
