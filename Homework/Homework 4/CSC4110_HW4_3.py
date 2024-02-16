#CSC 4110 HW4 P3 MAY WANDYEZ GQ5426 2/25/2024
"""
Customer needs a password simulator to do the following:
(a) create random passwords in perpetuity
(b) if the password is “acceptable,” it gets archived
(c) “unaccepted” passwords get deleted
(d) no less than 40 iterations 

Problem Three Requirements:
Customer rules of ‘accepted passwords’
include: “special symbols,” and password 
cannot be a word in a dictionary list;
“random” module to be imported. 
"""

#BEGIN
import random
pkeyalph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$&"
n = 50 #passwords to generate
MPL = [] #master password list


#populate the list
for i in range(0,n):
    tempstring = ""
    for j in range(0,12):
        #pick a random letter 
        tempchar = pkeyalph[random.randint(0,len(pkeyalph)-1)]
        #place it in the list
        tempstring += tempchar
    MPL.append(tempstring)
    
#check if the any password in the list is invalid
for i in MPL[:]:
    #inherently, if the password is entirely alphnum it doesn't include a special
    #symbol and thus fails the password rules. Similarly if it is alnum it MIGHT
    #be in the dictionary
    if i.isalnum() == True:
        MPL.remove(i)

print("Here are the successfuly passwords")
print("You can add your own sonification to this program by shouting the word yay!")
print("Shout the word yay when you read 'Say Yay' " )
print(MPL)
print("Say yay!")        

                

#END