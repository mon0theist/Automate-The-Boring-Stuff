#! /usr/bin/python
#
# ATBS - Chapter 16 - Random Chore Assignment Emailer
#
# Write a program that takes a list of people’s email addresses and a list of chores
# that need to be done and randomly assigns chores to people. Email each person
# their assigned chores. If you’re feeling ambitious, keep a record of each person’s
# previously assigned chores so that you can make sure the program avoids
# assigning anyone the same chore they did last time. For another possible feature,
# schedule the program to run once a week automatically.
#
# Here’s a hint: If you pass a list to the random.choice() function, it will
# return a randomly selected item from the list. Part of your code could look
# like this:
#
# chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
# randomChore = random.choice(chores)
# chores.remove(randomChore) # this chore is now taken, so remove it

import random, smtplib, pprint, shelve, os

# list of email addresses
email_list = ['alice@example.com', 'bob@example.com', 'cathy@example.com', 'dave@example.com']

# chore list
chore_list = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# keep track who did each chore last
# use shelve to keep track of previous chore_tracker
if not os.path.exists('chore_tracker_shelf_file'):
    chore_tracker = {'alice@example.com': '',
    'bob@example.com': '',
    'cathy@example.com': '',
    'dave@example.com': ''}
    shelf_file = shelve.open('chore_tracker_shelf_file')
    # first time running program
else:
    # all subsequent runs after the first
    shelf_file = shelve.open('chore_tracker_shelf_file')
    shelf_values = list(shelf_file.values())
    chore_tracker = shelf_values[0]

# randomly assign email_list[i] an item from chore_list
# but don't assign same chore two weeks in a row
for i in range(len(email_list)):
    random_chore = random.choice(chore_list)
    name = email_list[i]
    # check for same chore
    while chore_tracker[name] == random_chore:
        # pick a different chore
        random_chore = random.choice(chore_list)

    # assign chore after passing the while loop check
    chore_tracker[name] = random_chore
    chore_list.remove(random_chore)

print('Chores have been randomly assigned:\n')
pprint.pprint(chore_tracker)

# TODO: Email assigned chored to people
print('Connecting to Gmail...')
print('Recommend using App-Specific Password')
gmail_addr = input('Gmail Address: ')
gmail_pw = input('Password: ')
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(gmail_addr, gmail_pw)

for i in range(len(email_list)):
    name = email_list[i]
    smtp_obj.sendmail(gmail_addr, name, 'Subject: Chores Selection\nDear %s,\nYour randomly selected chore for this week is %s.' % (name, chore_tracker[name]))

# disconnect
print('Emails have been sent, disconnecting from SMTP Server...')
smtp_obj.quit()

# LAST STEP - saving the new/updated shelf file
shelf_file['chore_tracker'] = chore_tracker
shelf_file.close()
print('Shelf file saved/updated!')
