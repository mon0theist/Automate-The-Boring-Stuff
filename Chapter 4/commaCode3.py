# ATBS Chatper 4 Practice Projects
# Trying yet again after reviewing the chapter
# No looking at other/past solutions this time!
# Code from scratch! Should be able to use a for loop instead of while loop
################
#
# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with "and" inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

def comma_list(list_value):
    new_string = ''
    for i in range(len(list_value)-1):
        new_string += str(list_value[i]) + ', '
    print(new_string + 'and ' + list_value[-1]) # for testing purposes
    return new_string + 'and ' + str(list_value[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
comma_list(spam)
