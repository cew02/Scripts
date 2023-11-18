# Random country picker. Make your travels random and special with select countries

import random

# Name of country: (average plane ticket price)
Countries = [['Germany', 1909], ['Australia', 9049], ['Ireland', 1110]]

while True:
    print('Fly to a random country?')

    user = int(input('1. Yes     2. Nevermind'))
    if user == 1:
        count = random.randint(1,3)
        if count == 1:
            print(Countries[0])
        elif count == 3:
            print(Countries[2])
        else:
            print(Countries[1])
    else:
        break
    
