# Let's analyze some text!
text = "Walking is falling forward. Each step we take is an arrested plunge, a collapse averted, a disaster braked. In this way, to walk becomes an act of faith. We perform it daily: a two-beat miracle-an iambic teetering, a holding on and letting go. For the next seven years I will plummet across the world."

sentences = text.split(".") # tokenize
# How many sentences in this text?
num_sentences= len(sentences)
total_words=0
for sentence in sentences:
	words = sentence.split(" ")
	num_words = len(words)
	total_words= total_words + num_words
# Average words per sentence?
words = sentences[0].split(" ")
num_words = len(words)

# Average length of a word in a sentence
words=text.split(" ")


# Number of vowels?
vowels=["a","e","i","o","u", "A", "E", "I", "O", "U"]
num_vowels=0
for letter in text:

#	for vowel in vowels:
#		if letter == vowel:

	if letter in vowels: # is letter a vowel? is letter in the list vowels?
		num_vowels=num_vowels+1
print num_vowels



print num_sentences
print total_words
