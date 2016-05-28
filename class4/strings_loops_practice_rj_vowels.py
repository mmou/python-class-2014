str_text = "Walking is falling forward. Each step we take is an arrested plunge, a collapse averted, a disaster braked. In this way, to walk becomes an act of faith. We perform it daily: a two-beat miracle-an iambic teetering, a holding on and letting go. For the next seven years I will plummet across this world."
count = 0
vowels = "aeiuoAEIOU"
for letter in str_text:
	if letter in vowels:
            count += 1
print count




