# Mini-project #6 - Blackjack

import simplegui
import random
#http://www.codeskulptor.org/#user41_BRSx2yMPvl_6.py

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = "Hand contains"
        for i in range(len(self.hand)):
            string +=" " + str(self.hand[i])
        return string

    def add_card(self, card):
        self.hand.append(card)	

    def get_value(self):
        value = 0
        for i in range(len(self.hand)):
            value += VALUES[self.hand[i].rank]
        
        for i in range(len(self.hand)):   
            if self.hand[i].rank == 'A':
                if value+10<=21:
                    return value+10
                else:
                    return value            
        return value
                                 
    def draw(self, canvas, pos):
         for i in range(len(self.hand)):
                self.hand[i].draw(canvas,[pos[0]+i*90,pos[1]])
                
            
            # draw a hand on the canvas, use the draw method for cards
         

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        string = "Deck contains"	
        for i in self.deck:
            string += " " + str(i)
        return string
    
#define event handlers for buttons
def deal():
    global note, in_play, score
    global deck, player, dealer,outcome
    if in_play == True:
        outcome = "You lose!"
        in_play = False
        score -= 1
        
        
        
    outcome = ""
    note = "Hit or Stand?" 
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    for i in range(2):
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
           
      
    in_play = True

def hit():
    global deck, player, dealer
  
    
    
    if player.get_value()<=21:
        player.add_card(deck.deal_card())
        
       
    if player.get_value()>21:
        stand()
    
def stand():
    global deck, player, dealer, note, in_play, outcome, score
    
    in_play = False
    
    note = "New Deal?"
    
    if player.get_value() > 21:
        outcome = "You went bust and lose!"
        score -= 1
        print player.get_value()
        print dealer.get_value()
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            
        if dealer.get_value() > 21:
            outcome = "Dealer went bust, You win!"
            score += 1
        else:
            if player.get_value() <= dealer.get_value():
                outcome = "You lose"
                score -= 1
            else:
                outcome = "You win"
                score += 1
   
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    #global player, dealer, outcome, in_play
    canvas.draw_text('Blackjack', (120, 60), 60, 'Black', 'monospace')
    canvas.draw_text(note, (190, 150), 40, 'White', 'sans-serif')
    canvas.draw_text('[SCORE : '+str(score)+']' , (475, 48), 20, 'White', 'sans-serif')
    canvas.draw_text(outcome, (120, 210), 40, 'Red', 'sans-serif')
    canvas.draw_text('Dealer', (25, 260), 40, 'Blue', 'serif')
    canvas.draw_text('Player', (25, 460), 40, 'Blue', 'serif')
    dealer.draw(canvas,[25, 280])
    player.draw(canvas,[25, 480])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, [25 + CARD_CENTER[0], 280 + CARD_CENTER[1]], CARD_SIZE)

    
    
    
    
    
    
    """card = Card("S", "A")
    card.draw(canvas, [25, 450])
    card.draw(canvas, [25, 250])"""
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
