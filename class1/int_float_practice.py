# PART I: Celsius to Fahrenheit converter!
#	take in a celsius temperature from the user (use raw_input)
#	print out a sentence to tell the user what the corresponding fahrenheit temperature is

#raw_input("What's the celsius temperature?") asks the user a question.
#	The user puts in an answer (for example, 50)
#	We store the answer (a string "50") in the variable celsius_string
celsius_string = raw_input("What's the celsius temperature?")

# cast the string celsius_string into a float
celsius = float(celsius_string) # what happens when you do int(celsius_string) instead?

# do math! store the answer in fahrenheit
fahrenheit = celsius * 9 / 5  + 32

# print the answer to the user using string formatting syntax
print "The fahrenheit temperature is %f" % fahrenheit




# PART II: Fahrenheit to Celsius converter!
#	take in a f temperature from the user (use raw_input)
#	print out a sentence to tell the user what the corresponding c temperature is

# YOUR CODE HERE