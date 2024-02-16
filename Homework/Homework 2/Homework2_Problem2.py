#HOMEWORK 2 PROBLEM 2 MAY WANDYEZ GQ5426
#BEGIN

#This program formats things to look like a letter.
# It does this line by line
#it uses various function to create each line.
#whoops, forgot strings were immutable FOR SOME REASON
def addInBulk(line, addthis, amount):
    for i in range(0,amount):
        line += addthis
    return line

def postageStamp(line):
    line = line[:-6] + "###" + line[-3:]
    return line

def envelopFrontBack(line):
    line = "|" + line[1:-1] + "|"
    return line


def envelopeToporBottom(line):
    line = "+" + line[1:-1] + "+"
    return line

def addressLine(line, address, l):
    middleindex = l // 2
    j = 0
    for i in range(middleindex, middleindex + len(address)):
        line = line[:i] + address[j] + line[i+1:]
        j += 1
    return line

def letterFormatter(name,  street,  city, state,  zip, l):
    #Create top or bottom of envelope
    line1 = ""
    line2 = ""
    line1 = addInBulk(line1, "_", l)
    line2 = addInBulk(line2, "_", l)
    line1 =envelopeToporBottom(line1)
    line2 =envelopeToporBottom(line2)
    print(line1)
    
    #create generic blank line
    linegen = ""
    linegen = addInBulk(linegen, "=", l)
    linegen = envelopFrontBack(linegen)
    
    
    
    #Create postage stamp lines
    line3 = ""
    line3 = addInBulk(line3,"=", l)
    line3 = envelopFrontBack(line3)
    line3 = postageStamp(line3)
    line4 = line3
    line5 = line3
    line6 = line3
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    
    #create blank lines between actual address
    line7 = linegen
    line8 = linegen
    print(line7)
    print(line8)
    
    #create addresslines =
    line9 = linegen
    line10 = linegen
    line11 = linegen 
    line9 = addressLine(line9, name, l)
    line10 = addressLine(line10, street, l)
    temp = city + ", " + state + " " + zip
    line11 = addressLine(line11, temp, l)
    print(line9)
    print(line10)
    print(line11)
    
    line12 = linegen
    print(line12)
    
    #print bottom of envelope
    print(line2)

    




name = "May Wandyez"
street = "42 W Warren Avenue"
city = "Detroit"
state = "MI"
zip = "48202"

letterFormatter(name, street, city, state, zip, 45)


    
    

#END