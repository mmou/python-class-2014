# use a while loop to continue to ask for guesses, UNTIL the user guesses correctly.

answer = 5
guess = 0
while guess != answer:
	guess = int(raw_input("guess my number?"))
	if guess > answer:
		print "too big"
	elif guess == answer:
		print "yeah 5 was my number!"
	else:
		print "too small"

#	secret_number = int(raw_input("guess my number?"))
#	if secret_number > answer:
#	  print"too small!"
#	elif secret_number < answer:
#	  print"too big!"
#	else:
#	  print"yep, 5 was my number!"
#	