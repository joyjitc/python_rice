# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random
def name_to_number(name):

	if name=='rock':
		return 0
	elif name=='Spock':
		return 1
	elif name=='paper':
		return 2
	elif name=='lizard':
		return 3
	elif name=='scissors':
		return 4
	else:
		print 'error_name2num'
		return -1

# convert name to number using if/elif/else
# return the result
def number_to_name(number):

	if number==0:
		return 'rock'
	elif number==1:
		return 'Spock'
	elif number==2:
		return 'paper'
	elif number==3:
		return 'lizard'
	elif number==4:
		return 'scissors'
	else:
		return 'error_num2name'

# convert number to a name using if/elif/else
# return the result!


def rpsls(player_choice): 

	print ""
	print "Player chooses",player_choice
	player_number=name_to_number(player_choice)
	comp_number=random.randrange(0,5)
	comp_choice=number_to_name(comp_number)
	print "Computer chooses",comp_choice
	decision=(comp_number-player_number)%5
	if decision==0:
		print 'Player and Computer tie!'
	elif decision<3:
		print "Computer wins!"
	else:
		print "Player wins!"


# print a blank line to separate consecutive games

# print out the message for the player's choice

# convert the player's choice to player_number using the function name_to_number()

# compute random guess for comp_number using random.randrange()

# convert comp_number to comp_choice using the function number_to_name()

# print out the message for computer's choice

# compute difference of comp_number and player_number modulo five

# use if/elif/else to determine winner, print winner message
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
