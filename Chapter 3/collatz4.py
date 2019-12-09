# ATBS Chapter 3
# Doing collatz again for review

import sys

# defining the collatz function
def collatz(number):
    if number % 2 == 0:
        # print(number // 2)
        return number // 2
        # // is floor-division, drops everything after decimal
    elif number % 2 == 1:
        # print(3 * number + 1)
        return 3 * number + 1


while True:
    try:
        userNum = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Error: Please enter an integer value')

while userNum != 1:
    userNum = collatz(userNum)
    print(userNum)
