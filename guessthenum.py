# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simpleguitk as simplegui


# helper function to start and restart the game
def new_game():
    range100()
    
    # initialize global variables used in your code here

    


# define event handlers for control panel
def range100():
    global secret_number, tries
    secret_number = random.randrange(0,100)
    tries = int(math.ceil(math.log(100,2)))
    global type
    type=tries
    print "New game. The range is from 0 to 100"
    print "Number of remaining choices is ",tries
    print ""
    # button that changes the range to [0,100) and starts a new game 
    
    


def range1000():
    global secret_number, tries
    secret_number = random.randrange(0,1000)
    tries = int(math.ceil(math.log(1000,2)))
    global type
    type=tries
    print "New game. The range is from 0 to 1000"
    print "Number of remaining guesses is ",tries
    print ""
    # button that changes the range to [0,1000) and starts a new game     
    
    
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was ",guess

    global tries
    tries-=1
    print "Number of remaining guesses is",tries


    if tries!=0:
        if secret_number<guess:
            print "Lower!"
        elif secret_number>guess:
            print "Higher!"
        else:
            print "Correct!"
            print ""
    else: 
        if guess==secret_number:
            print "Correct!"
            print ""
        else: 
            print "You ran out of guesses. The number was ",secret_number
            print ""
        if type==7:
            range100()
        else:
            range1000()

    print ""


    # main game logic goes here 
    
    
    
# create frame
frame=simplegui.create_frame("Guess the number!!",200,200)
frame.add_input("Enter a Guess!",input_guess,50)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
new_game()

frame.start()


# register event handlers for control elements and start frame

# call new_game 

