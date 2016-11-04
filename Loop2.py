def checkanswer(guess,correctanswer):	if guess==correctanswer:		return "Congrats!"	elif guess<correctanswer:		return "Try higher"	elif guess>correctanswer:		return "Try lower"	else:		print "Pick a number."
	#[HERE YOU NEED TO COMPARE THE GUESS TO THE CORRECT ANSWER AND RETURN A RESULT]correct=0
count=0 
correctanswer=7

while (correct<1 and count<20):	guess=raw_input("Enter a number 1-20: ")
	result=checkanswer(int(guess),correctanswer)	if result=="Congrats!":		correct=2	print result
	#[HERE YOU NEED TO PROVIDE A PROPER RESPONSE TO THE USER, BASED ON THE RESULT OF THE COMPARISON]
	count+=1;
