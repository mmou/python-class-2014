# use a while loop to continue to ask for guesses, UNTIL the user guesses correctly.

def guess_my_number():
	while guess != answer:
		guess=int(raw_input("guess my number?"))
		guess=guess
		if guess > answer:
			print "too big"
		if guess < answer:
			print "too small"
	if guess == answer:
		print "yep, %s was my answer" % answer

guess_my_number(20)
guess_my_number(10)
guess_my_number(80)