# Ch 4 Practice Project - Comma Code
# second attempt
#
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item. For example, passing the previous spam list to the function
# would return 'apples, bananas, tofu, and cats'. But your function should be
# able to work with any list value passed to it.
#
# Couldn't figure this out on my own, had to look at the solution from my last attempt,
# which I'm also pretty sure I didn't figure out on my own, pretty sure I
# copy+pasted from somewhere
#
# I can read it and understand why it works, but writing it from scratch is a whole
# different thing :'(

def commaList(listValue):
    counter = 0
    newString = ''
    while counter < len(listValue)-1:
        newString += str(listValue[counter]) + ', '
        counter += 1
    print(newString + 'and ' + str(listValue[counter])) # print for testing
    return newString + 'and ' + str(listValue[counter])

spamList = ['apples', 'bananas', 'tofu', 'cats']
commaList(spamList)
