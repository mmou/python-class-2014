# use a while loop to continue to ask for guesses, UNTIL the user guesses correctly.

answer = 27
guess = 0

while guess != answer:
	if guess > answer:
		print "too djfk"
	else:
		print "sjdks"
	guess = int(raw_input("guess my number?"))

secret_number = int(raw_input("guess my number?"))
if secret_number > answer:
  print"too small!"
elif secret_number < answer:
  print"too big!"
else:
  print"yep, 27 was my number!"
