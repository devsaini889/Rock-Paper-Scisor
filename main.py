#A small chid game of rock ,spaper ,scisors


import random

def game_data(pc,you):
    if(pc==you):
        return None
    elif (pc=='r'):
        if (you=='p'):
            return True
        elif(you=='s'):
            return False
    elif(pc=='p'):
        if(you=='s'):
            return True
        elif(you=='r'):
            return False
    elif(pc=='s'):
        if(you=='r'):
            return True
        elif(you=='p'):
            return False
    

print(" A game with pc: Rock, Paper , scisors......")
randnum = random.randint(1,3)
if randnum == 1:
    pc = "r"
elif randnum == 2:
    pc = "p"
elif randnum == 3:
    pc = "s"
else:
    print("Invalid Option.")

    

you = input(" Input the option you want to choose(rock,paper,scisor) : ")
   
gamestatus = game_data(pc, you)

print(f"\nComputer Choice {pc} and Your Choice {you}")

if(gamestatus == None):
     print("\nGame Tie")
elif(gamestatus):
    print("\nCongratulations, You've Won the Game...!")
else:
     print("\nYou've Lost the Game, Better Luck Next Time...")


