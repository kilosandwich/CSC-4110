#MAY WANDYEZ GQ5426 CSC 3110 HOMEWORK 3 PROBLEM 2
#BEGIN
#INSTRUCTIONS:
"""
Write a program 
that uses automation 
to procedurally use adjacencies
to take value from the old list and
create values in the new list. 
Recall that each neighbor i
n the new list is the sum of 
he immediate adjacent neighbors.
"""

def adjacener(list1):
    #create a list the size of the first list.
    templist = [0]*len(list1)
    #End points of list are exceptions
    templist[0]=list1[0] + list1[1]
    templist[-1] = list1[-1] + list1[-2]
    #Iterate through middle of the list
    for i in range(1,len(list1)-1):
        templist[i] = list1[i-1]+list1[i+1]
    print(templist)

oldList =[78,56,8,12,90,21,71,98,101,1245,1600]

adjacener(oldList)


#END
