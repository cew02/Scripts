import random

print('Pick a number 1-100?')

while True:
    user = int(input('1. Number    2. Exit'))
    if user == 1:
        number2 = random.randint(1,1000)
        print(number2)
    else:
        break
    
