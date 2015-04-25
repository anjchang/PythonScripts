from time import sleep
import serial
ser = serial.Serial('/dev/tty.usbmodemfa131',9600) #connection on port          
counter = 32 #below 32 everything in ASCII is gibberish                         
while True:
    counter +=1
    #ser.write(str(chr(counter))) # Convert dec number to ASCII send to arduino
    print ser.readline() # read data from arduino                               
    sleep(.1) # delay for tenth of second                                       
    if counter ==255:
        counter = 32

