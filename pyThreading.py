from threading import Thread
import time
import serial, string


active = True
input_number = 0


def input_rfid():
    global active
    global input_number
    
    input_number = input()
    time.sleep(0.3)
    if(input_number != 0):
        active = False

    
thr1 = Thread(target=input_rfid)
thr1.start()


mag_reader = " "
ser = serial.Serial('/dev/ttyUSB0',9600,8,'N',1,timeout=1)
while active:
    #print("---START--")
    while active:
        mag_reader = ser.readline()
        #print(len(output))
        if(len(mag_reader) > 0):
            temp1 = str(mag_reader.decode('utf-8'))
            temp2,temp3 = temp1.split('+')
            input_number = temp3.rstrip('?\r\x03').replace(' ','')
            #print("Break")
            break
         
    #print("---STOP--")
    break
 


print("input_number : ",input_number)


