# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

def new_game():
    '''
    Helper function to start and restart the game 
    with all needed global variables.
    '''
    global secret_number, n
    secret_number = random.randrange(0, height)
    n = math.ceil( math.log(height + 1, 2) )
    print 'New game started'
    print 'The secret number is less then ' + str(height) + '.'
    print str(n) + ' guesses left.'
    print
    
# Event handlers for control panel
def range100():
    ''' 
    Button that changes the range to [0,100) 
    and starts a new game 
    '''
    global height
    height = 100
    new_game()
    
def range1000():
    '''
    Button that changes the range to [0,1000) 
    and starts a new game     
    '''
    global height
    height = 1000
    new_game()
    
    
def input_guess(guess):
    '''
    Takes the input guess string converts it to an integer, 
    and prints out a message
    '''
    global n	
    print 'Guess was ' + guess
    guess = int(guess)
    if guess < secret_number:
        print 'Higher'
        n -= 1
        print str(n) + ' guesses left.'
    elif guess > secret_number:
        print 'Lower'
        n -= 1
        print str(n) + ' guesses left.'
    else:
        print 'Correct'
        print 'Congratulations! You win!'
        print 'Starting a new game.'
        print
        new_game()
        
    if n == 0:
        print 'No more guesses left. You loose.'
        print 'Starting a new game.'
        print
        new_game()
    print

# GUI block    
frame = simplegui.create_frame('"Guess the number" game', 200, 200)
input_field = frame.add_input('Input your guess here:', input_guess, 150)
button_range100 = frame.add_button('Range 100', range100)
button_range1000 = frame.add_button('Range 1000', range1000)

frame.start()
height = 100
new_game()