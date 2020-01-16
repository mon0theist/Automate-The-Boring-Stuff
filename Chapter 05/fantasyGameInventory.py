# ATBS Chapter 5
# Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# defining the dictionary

def displayInventory(inventory): # displayInventory function has one argument
    print("Inventory:") # prints this string on it's own line
    item_total = 0 # counter variable, starting at 0
    for k, v in inventory.items(): # .items() displays key:value tuples, so for each tuple the first value (keys) gets assigned to k, the second value (values) gets assigned to v
        # FILL IN THE CODE HERE
        print(v, k) # prints the quantity of item followed by item name
        item_total += v # for every item printed, increases the item_total counter variable
    print("Total number of items: " + str(item_total)) # should be 62

displayInventory(stuff) # calls the function on the 'stuff' dictionary



##########################################################
# ATBS Chapter 5
# List to Dictionary Function for Fantasy Game Inventory
##########################################################

# totally lost on this, had to copy a github solution :(

# The setdefault() method offers a way to do this in one line of code. The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key does not exist. If the key does exist, the setdefault() method returns the key’s existing value that's already there.

def addToInventory(inventory, addedItems): # function takes two arguments
    # your code goes here
    for i in addedItems: #increments over the addedItems list, which will be dragonLoot in this case
        inventory.setdefault(i, 0) # checks inventory dict for key 'i' (which is iterating though the addedItems list), if doesn't exist, create and set value to 0 {i:0}; if it DOES exist, it just returns the current value for the key
        inventory[i] = inventory[i] + 1 # inventory[i] refers to the value stored at key 'i'; this increments the value of key 'i' by 1. Whether the item already existed or was created by the previous inventory.setdefault() function, either way it still needs to be incremented by 1.
    return(inventory) # returns the now merged inventory dictionary

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv) # displays the new inventory using the previous function
