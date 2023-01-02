import os
from time import sleep
import sys
import random

# essential variables

balance = 5
fruit = ['🍇', '🍊', '🍎', '🥝', '🍆', '💎', '🌟', '🥦', '🥓']
slot_1 = "X"
slot_2 = "X"
slot_3 = "X"
rolls = 0

# essential functions

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #- clear term



def waiting_animation(): #- animation
    line = ""
    for x in range(1, 3):
        while len(line) < 4:
            print(line)
            line += "."
            sleep(0.3)
            clear()
        line = ""
    pass

# main game

while balance > 0:

    #- Printing of slot machine

    print("||"+slot_1+"||", "||"+slot_2+"||", "||"+slot_3+"||", '--- balance:', balance, '--- rolls:', rolls)
    
    
    input("Press 'enter' to roll the machine: ")
    waiting_animation()
    
    #- Number gen
    
    i = random.randint(0, 8)
    slot_1 = fruit[i]
    i = random.randint(0, 8)
    slot_2 = fruit[i]
    i = random.randint(0, 8)
    slot_3 = fruit[i]

    
    #- Points calculator
    if slot_1 == slot_2 or slot_2 == slot_3: #- 2 in a row
        balance += 2
    if slot_1 == slot_2 == slot_3:
        balance += 5
    if slot_1 == slot_2 or slot_1 == slot_3 or slot_2 == slot_3:
        balance += 1
    else:
        balance -= 1

    rolls += 1

print("You lost!")
input("Open and close the program to play again.")