correct=0
cnt=0 
question= raw_input("Enter a number 1-20: ")
def answer(n):
	while (correct<1 and cnt<20):
		if n==7:
			break
			print "Correct!! We have a winner!"
	if n<7:
		return "You are aiming too low"
	elif n>7:
		return "Youre aiming too high"
	else:
		print "Enter a number"
cnt+=1;
