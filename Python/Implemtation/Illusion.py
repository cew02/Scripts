import random

print('I want to play a game. 1. Yes      2. No')

user = int(input())

if user == 1:
    print('Choose a number between one and ten')
else:
    print('You get the illusion of choice hehe :3. Pick a number between one and ten.')

loss = random.randint(1,10)
user2 = input(range(1,10))

if user2 == loss:
    print('You Win! Yipee! :D')
else:
    print('You Lose :(')