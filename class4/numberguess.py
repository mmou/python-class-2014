answer = 27
guess = 0

while guess != answer:
	guess = int(raw_input("guess my number?"))
	guess = guess
    	if guess  > answer:
    		print "you should guess lower"
    	if guess < answer:
    		print "you should guess higher"
if guess == answer:
	print "you got it!"

 

