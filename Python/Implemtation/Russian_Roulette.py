import random

print('We are going to play a game. 1. Ok     2. No')
user = int(input())

if user == 1:
    print('Pick a number between 1 and 6')
else:
    print('The illusion of choice hehehe :3. Pick a number between 1 and 6')

shot = random.randrange(1,6)
user2 = input(range(1,6))

if user2 == shot:
    print('You Lose!')
else:
    print('You Win! YAY!')
