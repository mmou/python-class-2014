# Let's analyze some text!
text = "Walking is falling forward. Each step we take is an arrested plunge, a collapse averted, a disaster braked. In this way, to walk becomes an act of faith. We perform it daily: a two-beat miracle-an iambic teetering, a holding on and letting go. For the next seven years I will plummet across the world."

# How many sentences in this text?	
sentences = text.split(".") # tokenize
num_sentences = len(sentences)



# Average words per sentence?

# solution 1
total_words = 0
for sentence in sentences:
	words = sentence.split(" ")
	num_words = len(words)
	total_words = total_words + num_words

ave_words_per_sentence = total_words/num_sentences


# solution 2
all_words = text.split(" ")
total_words = len(all_words)
ave_words_per_sentence = total_words/num_sentences


# this is just the number of 
# words in the 1st sentence!
words = sentences[0].split(" ")
num_words = len(words)

# Average number of letters in a word?

words = text.split(" ") #list of the words



# Number of vowels in the text?
