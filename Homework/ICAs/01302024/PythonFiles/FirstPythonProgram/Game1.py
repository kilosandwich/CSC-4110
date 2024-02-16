#MAY WANDYEZ GQ5426 CSC 4110 ICA GAME 1
#Begin
"you bet if the coin flip goes your way or not"
import random,sys
from tkinter import *

def game1():
    game = True
    while(game == True):
        inputgoeshere = ""
        coinflip = random.randint(0,1) #0 for heads, 1 for tails
        coinoptions = ["heads", "tails"]
        coinflip = coinoptions[coinflip]
        
        while( (inputgoeshere != "heads") and (inputgoeshere !="tails") and (inputgoeshere != "quit")):
            inputgoeshere = input("heads or tails?\n (type 'quit' to quit, you quitter)")
        if inputgoeshere == "quit":
            break
        print("The coin flips, the result is: ", coinflip)
        
        if (inputgoeshere == coinflip):
            print("You win, you feel a sense of pride and acomplishment")
        else:
            print("You lose, you feel a fear of missing out, maybe a microtransaction would help")
        
        

def game2():
    game = True
    while(game == True):
        print("You see a ball coming at you, what do you do?")
        inputgoeshere = ""
        inputgoeshere = input("Type 1 to hit the ball,\n type 2 to not hit the ball,\n type 3 to quit")
        returnchance = random.randint(1,3)
        if(inputgoeshere == "1"):
            print("You hit the ball back at your opponent")
        elif(inputgoeshere == "2"):
            print("""You relent to the inevitable, the wall celebrates in victory.\n You were playing tennis against a ltieral wall, and you will
never be as good as him""")
        else:
            break
        
def quit():
    print("Why must you always disappoint me")
    sys.exit()
    
    
#TKINTER nonsense
root = Tk()
win =Frame()
win.pack()

labelfont = ('times', 30 ,'bold')
widget = Label(win, text='FUN GAMES BY MAY', font = labelfont).pack(side=TOP)

Button(win, text='COIN FLIPPING', command = game1).pack(side=TOP)
Button(win, text='TENNIS',command = game2).pack(side=TOP) 
Button(win, text = 'quit', command = quit).pack(side=TOP)
root.mainloop()


#ENd