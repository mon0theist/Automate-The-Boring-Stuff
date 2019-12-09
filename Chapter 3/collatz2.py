# The Collatz Sequence

def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return number * 3 + 1

runCode = True # variable for determining whether or not the entire program should loop

while runCode == True:
	while True: # User input loop, loops until user enters a valid integer
		try:
			userInt = int(input('Please enter a number:'))
			break
		except ValueError:
			print('Error: You have not entered an integer (whole number) value')		
	
	newInt = collatz(userInt) # Runs the collatz function on the user's inputted number, assigning to newInt
	print(newInt)

	while newInt > 1: # repeated Collatz sequence until number gets down to (1) 
		newInt = collatz(newInt)
		print(newInt)

	print("Your number " + str(userInt) + " has been Collatz'd!")
	print("Math is hard")
	input bool('Would you like to Collatz another number? (y/n)') # convert input string to True or False bool?
	# How do I take the user's input and have that determine whether or not the program runs again?
	
	
# Need to figure out how to make this entire thing loop, so at the end of the program, it will ask whether or
# not the user wants to run it again