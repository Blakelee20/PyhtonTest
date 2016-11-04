import time#imports time
import serial#imports serial

def getLatLonData():#defines a function
	latlon=[]#?
	f = open("gpsdata.txt","r")#opens and reads text file?
	str = "GPGGA"#sets str= to GPGGA
	for line in f:# for loop
		if(line.find(str)>0):#im not sure what this is really doing
			vals = line.split(',')
			#print vals[2]+vals[3]+', '+vals[4]+vals[5]
			latlon.append(vals[2])
			latlon.append(vals[4])#appends 2 values
			f.close()
			return latlon#returns latitude and longitude


ser = serial.Serial(
	port='/dev/ttyAMA0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)#setting variables?
counter=0
#f = open("gpsdata.txt","w")#reading text file?

while 1:
	latlon=getLatLonData()
	print latlon
	counter+=1
	if(counter>10):
		break#loop that records data and stops when data changes
#f.close()