#MAY WANDYEZ GQ5426 CSC 3110 HOMEWORK 3 PROBLEM 3
#2/1/2024
#BEGIN
#INSTRUCTIONS
"""
Write a program that uses automation
to procedurally separate five string
s having a name and phone number. 
The result is two separate collections
of names and phone numbers 
(they could be lists or strings).
"""

plist = []
nlist = []

def seperator(stringin):
    tempstringp = ""
    tempstringn =""
    for i in range(0,len(stringin)):
        if (stringin[i].isdigit()) or (stringin[i] == '-'):
            tempstringp += stringin[i]
        elif (stringin[i].isalpha()) or (stringin[i] == ' '):
            tempstringn += stringin[i]
    #clean up blank spaces at the end of the name
    tempstringn = tempstringn.rstrip(" ") 
    plist.append(tempstringp)
    nlist.append(tempstringn)

seperator("John Q Public 541-233-7612")
seperator("Quincy P Mockingham 65-688-4949")
seperator("Jimathy Lemoyne 233-755-9393")
seperator("Hanmpton Regularson 133-233-2333")
seperator("McCoy Kinney 233-344-1414")
            
            
print(plist)
print(nlist)

#END