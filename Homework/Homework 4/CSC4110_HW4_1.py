#CSC 4110 HW 4 - MAY WANDYEZ GA5426 2/25/2024
#OBJECTIVES:
"""
Create a data collector method,
simulating user records with the
following attributes:
username, password, birthdate,
address, social security number,
productPurchased,salesperson.
This program procedurally
generates ‘sample’ data and stores that data. 

Feed data collector values into key-value pair.
For example, the user data may be an entire list 
sequence, which is then considered the 
‘value’ portion of a unique user ID key.

This key-value structure must be searchable.
For example, a user may be able to search
the entire data store for users in a certain state,
or see which users were handled by a certain salesperson (or sales ID).
"""
#BEGIN
import random
#create lists of pregenerated names to generate data from
MLul = ["Admin", "Guest", "Visitor"] #Usernames
MLpl = ["Hunter2", "Password", "qwertyuiop"] #passwords
MLbdl = ["09-26-1997", "01-01-1990","02-02-1991"] #birthdays
MLal = ["123 Fake Street", "321 Example Avenue", "111 Thunder Road"] #addresses
MLsl = ["321-21-2121","243-35-5665","875-34-5423"] #Social security numbers
MLspl = ["Brett Sales", "Johnathan Sellers", "Greg Closing"] #Salespersons
MLppl = ["Pencils", "Books", "Large Books"] #Items
#create the masterlist
ML = []


#generate the fake data
n = 20 #number of fake data to generate
for i in range(0,n):
    tempid = "ID-" + str(i+1) #this is the key value pair, technically you could use a dictionary
    #generate the random data
    randul = MLul[random.randint(0,len(MLul)-1)]
    randpl = MLpl[random.randint(0,len(MLpl)-1)]
    randbdl = MLbdl[random.randint(0,len(MLbdl)-1)]
    randal = MLal[random.randint(0,len(MLal)-1)]
    randsl = MLsl[random.randint(0,len(MLsl)-1)]
    randspl = MLspl[random.randint(0,len(MLspl)-1)]
    randppl = MLppl[random.randint(0,len(MLppl)-1)]
    #add the data to the master list
    templist = [tempid,randul, randpl,randbdl,randal,randsl,randspl,randppl]
    ML.append(templist)
#create the key value pair

#create master dictionary for search system
MD ={}
MD["ID"] = 0
MD["Username"] = 1
MD["Password"] = 2
MD["Birthday"] = 3
MD["Address"] = 4
MD["SSID"] = 5
MD["Salesperson"] = 6
MD["Items"] = 7


#create the search engine
while(True):
    print("""
Welcome to the main menu
Please type what you want to search for:
(ID, Username, Password, Birthday, Address, SSID, Salesperson, Items)""")
    user_input =input("Type what category you want to search for:")
    user_input2 =input("What do you want to search for in that category? Press enter for general search")
    if user_input == "":
        print(ML)
    elif user_input2 == "":
        for i in range(0,len(ML)):
            print(ML[i][MD[user_input]]) #prints every location in the master list that matches the key pair
    else:
        for i in range(0,len(ML)):
            if ML[i][MD[user_input]] == user_input2: #if checks the category for the search criteria
                print(ML[i])
    
                
        
#END