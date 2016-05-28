# Let's analyze some text!
str_text = "Walking is falling forward. Each step we take is an arrested plunge, a collapse averted, a disaster braked. In this way, to walk becomes an act of faith. We perform it daily: a two-beat miracle-an iambic teetering, a holding on and letting go. For the next seven years I will plummet across the world."
count=0
vowels="aeiouAEIOU"
for letter in str_text:
	if letter in vowels:
		count+=1
print count

str_text="Walking is falling forward. Each step we take is an arrested plunge, a collapse averted, a disaster braked. In this way, to walk becomes an act of faith. We perform it daily: a two-beat miracle-an iambic teetering, a holding on and letting go. For the next seven years I will plummet across the world."
punctuation=[".",",",":","-"]
count=0
for char in str_text:
	if char in punctuation:
		count+=1
letters=len(str_text)-count
words=len(str_text.split( ))
average=letters/words
print average