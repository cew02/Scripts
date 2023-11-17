import random

while True:
    print('Heads or tails?')
    user = int(input('1. Flip?     2. Exit'))
    if user==1:
        flip = random.randint(1,2)
        if flip == 1:
            print("Heads")
        else:
            print("Tails")
    else:
        break
