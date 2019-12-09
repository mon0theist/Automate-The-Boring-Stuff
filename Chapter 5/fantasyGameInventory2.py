# ATBS Chapter 5 Practice Project - Fantasy Game Inventory
# 2nd attempt for revision/review
# No looking at past solutions!
#
# Most of the code is already given in the problem, just need to fill it in

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

# EZPZ
