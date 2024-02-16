#MAY WANDYEZ GQ5426 2/1/2024 CSC 3110 HOMEWORK 3
#BEGIN
"""
INSTRUCTIONS
Write a program that procedurally generates ‘sample’ data 
and stores that data in list form, such as a ‘list of lists.’
Each entry will consist of order/vendor information such as usernames, 
web orders, product IDs, quantities, date of order, region, etc.. 
The specific column/ category names are up to you (see Requirements).

At least 5 columns of procedurally created data, stored as a lists,
within an overall list.
The columns can be of any data, but should be made to look
like a customer order list (date, product-ID, region, etc….)
There should be no less than 20 ‘rows’ of data auto-generated.
Details are left to the student; use past lectures and materials from texts provided.
"""
#I am too lazy to comment it, so I will explain it here
#Items in the list had designated lists to draw random items from
#This generated each portion of the list procedurally
#Get the source of randomness
import random

#Item list to select random items from
il = ["Pencil", "Binder", "Stapler", "Science Skeleton", "Ruler"]
#Cost list where position in list corresponds to item should've used a dictionary but ehhhh
cl = [1.99,19.99,99.99,0.99,59.99]
#Region list to select rep from
rl = ["East", "Central", "West", "South"]
#Rep list
repl = ["Jones", "Kivell", "Sorvino", "Andrew", "Smith", "Jamestown"]

#how long do we need this to be
inputn = 30
#create the master list
ml = []
print("Date, Region, Representative, Item, Quantity, Total Sale")
for i in range (0,inputn):
    templist = [0,0,0,0,0,0,0]
    dateM = random.randint(1,12)
    dateD = random.randint(1,28) #We don't do sales past the 28th, our computer system cannot handle it
    dateY = random.randint(2022,2024)
    date = "" + str(dateM) + "/" + str(dateD) + "/" + str(dateY)
    templist[0] = date
    
    templist[1] = rl[random.randint(0,len(rl)-1)]
    templist[2] = repl[random.randint(0,len(repl)-1)]
    templist[4] = random.randint(1,99)
    tempr = random.randint(0, len(il)-1)
    templist[3] = il[tempr]
    templist[5] = cl[tempr]
    templist[6] = templist[4] * templist[5]
    print(templist)
    ml.append(templist)


print(ml)
    

#END