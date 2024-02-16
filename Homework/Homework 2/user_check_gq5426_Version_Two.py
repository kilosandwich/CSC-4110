#Revision 1 BEGIN
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

"""
#master list to store users for version 1
ml = ""
#initial user input to initiate loop
user_input = input("Please enter a username:" )

#loop to continuously add usernames
while(user_input != "end" and user_input != "exit"):
    #Routine A use a for loop to filter, string used to add
    for i in user_input:
        if(i.isalpha()):
            ml += i
    ml += " "
    user_input = input("Please enter a username:" )
#END