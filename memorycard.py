# implementation of card game - Memory
# This a modified version with - 
#   elif state == 1:
#        if clicked!=click1:
#           state = 2
#           exposed[clicked]=True
#           click2 = clicked
#           turns+=1
# The submitted version being at http://www.codeskulptor.org/#user41_TSzY6iFhME_1.py
# The url for this version http://www.codeskulptor.org/#user41_TSzY6iFhME_2.py

import simplegui
import random


# helper function to initialize globals
def new_game():
    global card, exposed, turns, state
    card = range(8) + range(8)
    random.shuffle(card)
    exposed = [False] * 16
    turns = 0
    label.set_text("Turns = %s"%str(turns))
    state = 0
    

     
# define event handlers
def mouseclick(pos):
    global exposed, turns, state, click1,click2
    clicked = pos[0]//50
    if state == 0:
        state = 1
        exposed[clicked]=True
        click1 = clicked
    elif state == 1:
        if clicked!=click1:
            state = 2
            exposed[clicked]=True
            click2 = clicked
            turns+=1
    else:
        if card[click1] == card[click2]:
            pass
        else:
            exposed[click1] = exposed[click2] = False
        exposed[clicked] = True  
        click1 = clicked
        state = 1
    
    label.set_text("Turns = %s"%str(turns))
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card, exposed 
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([[i*50, 0],[(i+1)*50,0], [(i+1)*50, 100], [i*50, 100]], 1, 'Green', 'Green')
        else:
            canvas.draw_text(str(card[i]), (5+50*(i), 75), 75, 'White')
           
    for i in range(15):
        canvas.draw_line(((i+1)*50,0), ((i+1)*50,100), 1, 'Red')
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
