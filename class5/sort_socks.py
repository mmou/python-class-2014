import random

# You are the senior engineer at a sock sorting company, 
# and it's your job to count the number of red and blue 
# sock pairs!

# This code makes sock baskets with random 
# assortments of red and blue socks:

def simple_sock_basket(n):
    num = 0
    while num < n:
        if random.random() < 0.3:
        	yield "red"
        else:
        	yield "blue"
        num += 1

# For example, to make a new sock basket with 10 socks, you do:

my_sock_basket = simple_sock_basket(10)

# From your sock basket, you pull out one sock at a time
# by calling the next() function.

sock = my_sock_basket.next()


# All blue socks are identical, and all red socks are identical.
# So you can put any blue sock with another blue sock to make a pair.

# Write a function that returns the 
# number of red pairs and blue pairs
def count_red_blue_pairs(sock_basket):
	
	# initialize some variables to help you
	red_pile = 0
	blue_pile = 0

	# this code gets the next sock for you
	while True:
		try:
			sock = sock_basket.next()
#			print "color: %s" % sock

			# count the socks......
			if sock == "blue":
				blue_pile += 1
			else:
				red_pile += 1

		except:
			break
	
	# now we have the number of red socks and the number of blue socks...
	red_count = red_pile/2 # both are integers, so red_count is always rounded-down integer
	blue_count = blue_pile/2

	return blue_count, red_count

sock_basket10 = simple_sock_basket(10) # make a sock basket with 10 socks 
print count_red_blue_pairs(sock_basket10) # count the pairs


# Business is booming and now your company deals with more
# than just red and blue socks. Now you don't know what colors
# your socks might be beforehand.

# This is how your new sock baskets are created:

def complex_sock_basket(n):
    prob = {
    	"red": 0.1,
    	"blue": 0.3,
    	"green": 0.6,
    	"yellow": 0.7,
    	"purple": 0.8,
    	"orange": 1
    }
    num = 0
    while num < n:
    	rand = random.random()
        if rand < prob["red"]:
        	yield "red"
        elif rand >= prob["red"] and rand < prob["blue"]:
        	yield "blue"
        elif rand >= prob["blue"] and rand < prob["green"]:
        	yield "green"
        elif rand >= prob["green"] and rand < prob["yellow"]:
        	yield "yellow"
        elif rand >= prob["yellow"] and rand < prob["purple"]:
        	yield "purple"
        else:
        	yield "orange"

        num += 1

# Write a function that returns the number of pairs of socks
# for each sock color
def count_pairs(sock_basket):

	# use dictionaries to help you organize your information
	# key: string representing color, value: number of socks that are that color
	piles = { }

	# this code gets the next sock for you
	while True:
		try:
			sock = sock_basket.next()
			print "color: %s" % sock

			# count socks.....
			if sock in piles:
				piles[sock] += 1
			else:
				piles[sock] = 1

		except:
			break

	for color in piles:
		piles[color] #......

	return piles		


complex_socks = complex_sock_basket(10)
print count_pairs(complex_socks)



# simple_socks = simple_sock_basket(100)
# print count_red_blue_pairs(simple_socks)

# complex_socks = complex_sock_basket(1000)
# print count_pairs(complex_socks)
