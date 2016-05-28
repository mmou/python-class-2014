# define a function that takes in a dictionary representing
# someone's grade breakdown.
# output their overall grade

# EXAMPLE OF SOMEONE'S BREAKDOWN
# keys = grade categories
# values = alice's grade in each category
alice_breakdown = {
	"homework": 90,
	"quizzes": 78,
	"tests": 80,
	"participation": 80	
}

def overall_grade(personal_breakdown):
	# keys = grade categories
	# values = percentage of the final grade that the category contributes 
	breakdown = {
		"homework": 20,
		"quizzes": 30,
		"tests": 40,
		"participation": 20
	}
	categories = breakdown.keys()
	
	overall_grade = 0
	for category in categories:
		category_grade = breakdown[category] * personal_breakdown[category]
		overall_grade += category_grade
	return overall_grade





