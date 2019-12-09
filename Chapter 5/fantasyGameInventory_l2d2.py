# ATBS Chatper 5 Practice Project - Fantasy Game Inventory List to Dictionary
# 2nd attempt for revision/review
# No looking at past solutions!
#
# Some of the code is already given in the problem, just need to fill it in

# Display Inventory function from previous exercise
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))

# new Add To Inventory function
def addToInventory(inventory, addedItems):
    # your code goes here
    # check to see if "new" item exists in inventory - .get() method?
    # or maybe .setdefault()
    # if it does, increment by 1
    # if it doesn't, create it and set to 1
    for i in range(len(addedItems)):
        inv.setdefault(addedItems[i], 0)
        item_added = addedItems[i]
        inv[item_added] += 1
    return inv

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
