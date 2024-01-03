# Random Dice Roller

import random

while True:
    print('''1. Roll the dice!        2. Exit        ''')
    # Force user to input
    user = int(input('What do you want to do?/n'))
    if user==1:
     # Print a number 1 through 6
     number = random.randint(1,6)
     print(number)
     #If user picks 2
     
    else:
       break

