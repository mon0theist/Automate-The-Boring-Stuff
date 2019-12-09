def collatz(number):
    if number % 2 == 0: #if number is even...
        print(number // 2)
        return number // 2
    else: # if number is odd (could also do if number % 2 = 1)
        print (3 * number + 1)
        return (3 * number + 1)

try:
    userNum = int(input('Please enter a number:\n'))

    while userNum != 1:
        userNum = collatz(userNum)
except ValueError:
    print('Error: Please enter an integer')
