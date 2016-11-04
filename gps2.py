import time#imports time
import serial#imports serial

ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1#seems to be just setting variables
)
counter=0
f = open("gpsdata.txt","w")#is this just opening and reading information out of the text file?

while 1:
	x=ser.readline()
	f.write(x)
	counter+=1
	if(counter>1000):
		break#Loop that reads data until it is changed
f.close()
