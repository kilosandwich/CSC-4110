#Revision number BEGIN/START DATE
### I genuinely don't know what you meant by this format
### you have both specified a rigid guide to follow and
### loose descriptions for what to do. I am probably
### overthinking it. Please reconsider submission requirements
### for future assignments, I am spending more time fretting over format
### for the assignment than learning.
##Begin May Wadyez here 1/18/2024 

#Objective:
"""
Copy and paste stuff from boxes 1 though 5 on the python
website and paste the code here.

That means I need to
create the documentation showing I actually created the code.
Huzzah.
"""
#1: Practice using definitions using the fibonacci sequence
def fib(n):
    #assignment multiple variables on one line, WOW
    a,b =0,1
    while a < n:
        #end= replaces the default newline character with the specified character
        print(a, end=' ')
        #you can also do multiple equations on one line
        #this honestly seems more confusing.
        a, b = b, a+b
        #I commented out this line because it was adding a new line
        #print()
        
#prove the function works
fib(1000)

#2 List Comprehensions
fruits = ['Banana', 'Apple', 'Lime'] #why is is always fruits in a list???
loud_fruits = [fruit.upper() for fruit in fruits]
print() #forgot to add a new line, whoops
print(loud_fruits)
#demonstrate the enumerate function
print(list(enumerate(fruits)))

#3 Simple Artithmetic
#demonstration of arithmetic in python
print(1/2)
print(2 ** 3)
print(17/3)
print(17//3)

#4 For Loop On A List
numbers = [2,4,6,8]
product = 1

for number in numbers:
#I really must object to using an iterator so 
#similar to the name of the list
    product = product * number
print('The Product IS: ', product)


#Don't type anything past this, this is the end.
#End