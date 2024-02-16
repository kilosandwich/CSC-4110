#GQ5426 Async Assignment 1
#BEGIN
"""Task:
1. Create the following objects: 
String, List, Set, Tuple, Dictionary

2.	Use the TAB button to show methods for object

3.	Write a program 
that utilizes at least TWO METHODS per object-type.

Note that you didn't say the program had to do anything sensible
"""
s = "wow a string!"
s.capitalize()
print(s)
s.lower()
print(s)
#LIST unordered, changeable
l = ['l', 'i', 's', 't']
l.pop()
print(l)
l.insert(-1,'p')
print(l)
#SETS unordered and unchangeable NO DUPLICATES
se = {1,2,3,4,5,1}
se.add(99)
print(se)
se.pop()
print(se)
#ordered and unchagenable tuple
tu = ("tuple", "why not use a list", "really never used tuples")
print(tu.count("tuple"))
print(tu.index("tuple"))
#ordered, changeable, NO DUPLICATES (because you can't have two keys)
di = {"potato": 1, "tomato":2, "asparagus":3}
print(di.copy())
print(di.pop("potato"))
  
#END