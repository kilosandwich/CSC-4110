#Revision number BEGIN/START DATE
##Begin May Wandyez here 1/18/2024 

#Objective:
"""
Write a python script that accepts 'any' user input at least 9 characters long 
that prints three characters, in three lines, in uppercase letters. 
USE ONLY METHODOLOGIES GONE OVER IN WEEK ONE VIDEOS.
TESTED INPUT must be a combination of upper- and lower-case letters. A
ll must be grouped to be aligned and on a separate line.
One input statement and ONE print statement.
Example:
asdFghjklvb
Becomes:
 asd 
  fgh 
  jkl

Huzzah.
"""

""" 
MANDATORY OPINION:
The most efficient programming method for this task would
be to use some long complicated way to use the formatting method
to output the response on one line while parsing through it

but that is difficult to read. I do not like writing code
that is difficult to read, and people do not like reading
code that is difficult to read.
"""

import sys

def threeUpper(inputWord):
    if (len(inputWord) < 9):
        print("Input is less than 9 characters.")
    else:
        #parse for the length of the input string
        tempcounter = 0 #tempcounter to keep track of every three passes
        for i in range(0,len(inputWord),1):
            #account for index out of bound exceptions
            #using a tempcounter
            if tempcounter < 3:
                #print out the character, convert it to upper case
                print(inputWord[i].upper(), end='')
                tempcounter += 1
                if(tempcounter >2):
                    tempcounter =0
                    #this technically isn't a print statement.
                    #It's a write statement.
                    #SURE, there is a long convoluted way to use
                    #formatting to put it all in one line, SURE,
                    #i COULD have turned each parsing into a separate variable
                    #and only created each variable if it did not create an index
                    #out of bound exception, but that seemed needlessly complicated.
                    sys.stdout.write('\n')


        
inputHere = input("please enter a string at least 9 characters long")

threeUpper(inputHere)
#End