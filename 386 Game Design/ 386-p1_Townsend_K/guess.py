#!/usr/bin/python

# author: Kendall Townsend
# email: kendallcar@csu.fullerton.edu
# description: Uses the MyPRNG class this is the executable file and tells you whether you are warmer/colder

from MyPRNG import MyPRNG
import math, time, random, getopt, datetime

def main():
#take in a user inputted seed and if left blank use the current seconds of the time
    try:
	rseed = input('Enter seed for rng:(blank uses current second of time) ')
    except SyntaxError:
	rseed = None
    while(rseed == None):
	now = datetime.datetime.now()
	rseed = now.second
#take in a user inputted minrange and if left blank use 2 instructions say use 1 but it doesn't work with the formula
    try:
	minrange = input('Enter Minimum range number:(blank will use 1) ')
    except SyntaxError:
	minrange = None
    if(minrange == None):
	minrange = 1
#take in a user inputted maxrange and if left blank use 1000
    try:
	maxrange = input('Enter Maximum range number:(blank will use 1000) ')
    except SyntaxError:
	maxrange = None
    if(maxrange == None):
	maxrange = 1000
#initiate a new function random using the class myPRNG
    random = MyPRNG(minrange, maxrange)
    random.seed(rseed)
    randomnumber = 0
    guess = None
    lastguess = 0
    count = 1
#use a forloop to get the 101st random number to use for game as per instructions
    for test in range(102):
	count+=1
	if(count == 101):
		randomnumber = random.next_prn()
#here is the game part of the program telling people whether they are hot or cold based on their best guess
    while( randomnumber != guess):
#make sure they can't put in no input
	while(guess == None):
		try:
			guess = input('What do you think the number is? (0 to exit): ')
			#for first time through loop make sure first guess is the current best guess
			if( lastguess == 0 ):
				lastguess = guess
		except SyntaxError:
			guess = None
	if( guess == 0 ):
		print('Better luck next time!')
		print('The number was ( %d )' %randomnumber)
		guess = randomnumber
	elif( randomnumber == guess ):
		print(' You did it! ')
	elif( abs(randomnumber - guess) > abs(randomnumber - lastguess) ):
		print('Colder last guess ( %d ) was closer' %lastguess)
		guess = None
	else:
		lastguess = guess
		print('Warmer ( %d ) is now your closest guess' %guess)
		guess = None

if __name__ == "__main__":
    main()
