#Revision 2 BEGIN
#May Wandyez 1/25/2024
"""
ASSIGNMENT:
Write a program (programs) that prompts y
ou to add a username 
to a sequence (collection) of stored names.

 It must continuously prompt for more user names
 until a condition, such as typing ‘exit’ is met
 .

The company you work for has a policy that says
“no characters such as “#,^% or digits such as 
1,2,3,4,5,6,7 are ever used in usernames,” 
and all characters other than letters are 
filtered (see Version One and Version 
Two below for further detail).

VERSION 1
A ‘for loop’ is used to filter out unwanted characters; 
a STRING is used to store, add, and maintain users. 
This is to be referred to as ‘Routine A’ in your comments.

VERSION 2
You must NOT use a ‘for loop.’ Like Routine A, a STRING is used to store, add, and maintain users. 
This is to be referred to as ‘Routine B’ in your comments.

VERSION 3
It's version 1 except with a list instead of a string

VERSION 4
It's version 2 except with a list instead of a string
"""
#master list to store users for version 1
ml = []
#initial user input to initiate loop
user_input = input("Please enter a username:" )

#loop to continuously add usernames
while(user_input != "end" and user_input != "exit"):
    
   
    tempstr = ""
   
    #Routine D, don't use a forloop, but do the same thing
    temp = len(user_input)
    i = 0
    while(i<temp):
        if(user_input[i].isalpha()):
            tempstr += user_input[i] 
        i += 1
    
    ml.append(tempstr)
    
    user_input = input("Please enter a username:" )
#END