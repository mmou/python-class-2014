# dictionary with grade weights in percentages
breakdown = {
	"homework": 20,
	"quizzes": 30,
	"tests": 40,
	"participation": 20
}

# (1) how many categories make up your grade?
categories = breakdown.keys()
num_categories = len(categories)
print num_categories

#OR
print len(breakdown.keys())

#EASIEST WAY
print len(breakdown)


# (2) is the breakdown valid (does the total percentage = 100%)? (use a comparison operator)
	# calculate total percentage
	#if total percentage = 100%, print "yes it's valid!"
	# if it's not, print "nope it's not valid"
# YOUR CODE HERE

percentage = #I NEED TO GET THIS

# case 1: percentage > 100 or < 100 --> percentage != 100
if percentage == 100:
	print "yes it's valid!"

# case 2: percentage == 100
else:
	print "nope it's not valid"



# (3) if not, fix it (however you want, such that total percentage = 100%)
# YOUR CODE HERE

# (4) is 'essays' a grade category?
	# if 'essays' is a grade category, print "essays is a grade category!"
	# if 'essays' is NOT a grade category, print "essays is NOT a grade category!"	
# YOUR CODE HERE


# (5) Alice is in this class, and has a 90% in homework, 
# 80% in quizzes, 85% in tests, and 10% in participation.
# What is her overall grade?
overall_grade = 0 #YOUR CODE HERE