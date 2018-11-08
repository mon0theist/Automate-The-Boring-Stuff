# ATBS Chapter 4 - Comma Code
#
# 4th attempt for review/revision purposes
#
# No looking at other attempts or solutions!

spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = ['blueberries', 'pancakes', 'grapes', 'watermelon', 'apricots']
# second, longer test for testing purposes

def commaCode(listValue):
    for i in range(len(listValue[:-2])):
        print(listValue[i], end=', ')
    print('and ' + listValue[-1])

commaCode(spam)
commaCode(eggs)
