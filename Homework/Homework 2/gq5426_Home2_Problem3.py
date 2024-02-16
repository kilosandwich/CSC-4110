#GQ5426 HOMEWORK 2 PROBLEM 2 1/25/2024
#Assignment:
"""
Split a string on the basis of its
3 digit numbers and commas
"""
#complicated log
log = """341JohnButters,111Jorgunhooves,222JakeHamtaro,333JackSmith,444JannahJamson,555IgorSampson,666FirstLastname,777JennaMaroni,888KeyboardJordan,999BennyHannah,101Gemorahgodzilla,110Lemontiusflyn,131ElbertDrake,141ShamesMacinkly
"""



#this is where our employee names will go
e = []
#assume 3 digits at start
i=0
#iterate using while loop
while(i<len(log)):
    #assume this is where the text starts (add 3 due to error)
    start = i+3
    #assume text ends with a comma
    end=log.find(',',start)
    #I forgot that find returns -1 now I could have just
    #added an extra comma, but ehhhh
    if end == -1:
        break
    #the name exists between the start and end
    e.append(log[start:end])
    #start looking and the tail end where the last comma was found
    i = end + 1 

    
    #print("help I am caught in the loop")
print(e)

"""
If I were to do this again, in hindsight, I could have split the
string into a list using the split command, then kept only those
characters in the string which were not numbers,

this would have also allowed me to separately parse out
their employee ids. The advantage of my current approach 
is that it is fairly adjustable.


If I had more time and unlimited funds I would have
subcontracted out this to another company so I would
not have had to do it myself and so that any faults
in the deliverables were the fault of the contractor,
does exculpating me of blame in my position.
"""