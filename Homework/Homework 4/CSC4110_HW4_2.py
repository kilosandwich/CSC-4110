#CSC 4110 HOMEWORK 4 PROBLEM 2 MAY WANDYEZ GQ4526 2/15/2024
#OBJECTIVES
"""
Build a PIRATE themed game of chance with the following
(a) build and populate treasure chest with as many items customer requires
(b) create a bank / loot stash
(c) wagers to be placed per “spin” or treasure chest “grab”
(d) customer “plays” until bank account reaches 0 or below.
"""
#BEGIN
import random
lootOptions = ["Plank", "Ship", "Cannonball", "Piece of Eight"]
#size of the treasure chest
n = 20
TML = []
#populate the treasure chest with items from the list
for i in range(0,n):
    TML.append(lootOptions[random.randint(0,len(lootOptions)-1)])

#player win loot list, victory master list
VML = []
#player bank
BankBalance = 10

#gameplay
while(True):
    print("""
Welcome to Pirate Palooza, it costs 1 money to play
""")
    if BankBalance == 0:
        break
    
    print("You currently have: ", BankBalance, " money")
    user_input = input("Press enter to play, type anything else to exit")
    
    if user_input == "":
        #find a random number for the current length of the treasure list
        tempint = random.randint(0,len(TML))
        #add the loot to the player's treasure chest
        VML.append(TML[tempint])
        print("You won:", TML[tempint])
        #delete the item from the treasure pool
        BankBalance -= 1
        del TML[tempint]
    else:
        break

print("You won!")
print(VML)

    

#END