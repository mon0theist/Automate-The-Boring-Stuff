# ATBSWP Chatper 4 Practice Project 1
#
# Say you have a list value like this:
# 
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(aList):
	count=0 # counting variable
	aString='' # blank string that will be modified as the function executes
	
	while count < len(aList)-1: # all values before the final one
		aString += aList[count] + ', ' # adds the index, numbered by the count var, from the list that the function is running from (aList)
		count+=1 # adds to the counting var, which will continue until we get to len(aList) - 1
	return aString + 'and ' + aList[count] # returns aString, which was blank and has now been modified by the list values, indexed by the count var. then concatentates the 'and' string, followed by the final index in aList indicated by the current count var value

# The above function works, but only if the list contains string values. Doesn't work with int values. Will need to modify code to allow function to also work with int values

def comma2(aList):
	count=0 # counting variable
	aString='' # blank string that will be modified as the function executes
	
	while count < len(aList)-1: # all values before the final one
		aString += str(aList[count]) + ', ' # adds the index, numbered by the count var, from the list that the function is running from (aList). str() ensures that the value is a string, even if the list contains an int or float value
		count+=1 # adds to the counting var, which will continue until we get to len(aList) - 1
	return aString + 'and ' + str(aList[count]) # returns aString, which was blank and has now been modified by the list values, indexed by the count var. then concatentates the 'and' string, followed by the final index in aList indicated by the current count var value. str() must also be added to aList[count] due to TypeError: Can't convert 'int' object to str implicitly
	
print(comma(spam))

desk = ['computer', 'monitors', 'keyboard', 'mouse', 'phone', 'headset']

grades = [90, 95, 87, 100, 79, 85, 97, 88]
temps = [98.2, 88.8, 82.3, 90.1, 99.9]

print(comma(desk))

print(comma2(grades))

# comma2 function works regardless if values in string are strings or ints, will test for floats

print(comma2(temps))

# comma2 also works for floats! :) 
# comma is no longer needed