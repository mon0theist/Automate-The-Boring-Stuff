#!/usr/bin/python

# ATBS Chapter 10
# The following program is meant to be a simple coin toss guessing game. The
# player gets two guesses (it’s an easy game). However, the program has several
# bugs in it. Run through the program a few times to find the bugs that keep the
# program from working correctly.

# I didn't really use the debugging tools, just ran the program a couple times
# and then started looking at the code and fixing it

# import needed modules
import random, logging, traceback

# set logging level (copied from Chapter 10 example_)
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# disables logging, comment out the following line to re-enable debugging
logging.disable(logging.CRITICAL)
# commented out = logging/debugging ENABLED

# debug start
logging.debug('Start of program')

def guess():
    guess = ''
    while guess != 'heads' and guess != 'tails' and guess != 'h' and guess != 't':
        guess = str.lower(input('Guess the coin toss! Enter (h)eads or (t)ails: '))
        if guess == 'h':
            guess = 'heads'
        elif guess == 't':
            guess = 'tails'
    return guess

def toss():
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if toss == 0:
        toss = 'tails'
    elif toss == 1:
        toss = 'heads'
    return toss

def check():
    tries = 2
    user_guess = guess()
    tries = tries - 1
    coin_toss = toss()

    while tries > 0:
        if user_guess == coin_toss:
            print('You got it!')
            break
        elif user_guess != coin_toss:
            print('Nope! Guess again!')
            tries = tries - 1
            user_guess = guess()
    if tries == 0:
        print('Nope. There are only 2 choices...')

check()
