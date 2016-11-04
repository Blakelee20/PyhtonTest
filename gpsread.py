f = open("gpsdata.txt","r")
str = "GPGGA"
for line in f:#finds a line in the text file
	if(line.find(str)>0):#i dont know
		vals = line.split(',')
		#print vals[2]+vals[3]+', '+vals[4]+vals[5]
		print vals[2]+', '+vals[4]