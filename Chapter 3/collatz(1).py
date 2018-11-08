# The Collatz Sequence

def collatz(number):
	if number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		return number * 3 + 1


while True:
	try:
		userInt = int(input('Please enter a number:'))
		break
	except ValueError:
		print('Error: You have not entered an integer (whole number) value')		
	
newInt = collatz(userInt)
print(newInt)

while newInt > 1:
	newInt = collatz(newInt)
	print(newInt)

print("Your number " + str(userInt) + " has been Collatz'd!")
print("Math is hard")

# Need to figure out how to make this entire thing loop, so at the end of the program, it will ask whether or
# not the user wants to run it again