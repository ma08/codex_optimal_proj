
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100
secret_number = 0
remaining_guesses = 7
# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    pass
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range, secret_number, remaining_guesses
    num_range = 100
    remaining_guesses = 7
    secret_number = random.randrange(0, num_range)
#    print secret_number
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is", remaining_guesses
    print ""
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, secret_number, remaining_guesses
    num_range = 1000
    remaining_guesses = 10
    secret_number = random.randrange(0, num_range)
#    print secret_number
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is", remaining_guesses
    print ""
def input_guess(guess):
    # main game logic goes here	
    global remaining_guesses, secret_number, num_range
    guess = int(guess)
    print "Guess was", guess
    remaining_guesses -= 1
    print "Number of remaining guesses is", remaining_guesses
    if remaining_guesses == 0:
        print "You ran out of guesses. The number was", secret_number
        print ""
        new_game()
    elif guess > secret_number:
        print "Lower!"
        print ""
    elif guess < secret_number:
        print "Higher!"
        print ""
    else:
        print "Correct!"
        print ""
        new_game()
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
# register event handlers for control elements
# call new_game and start frame
new_game()
frame.start()
