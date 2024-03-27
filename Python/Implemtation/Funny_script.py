import random

user = int(input('Do you want me to pick a random number? 1. Yes      2. No'))

if user == 1:
    print('Yipee!')
    print(random.randrange(1,1999999999))
else:
    print('W-w-w-why not? ;~;')
    input()
    print('Oh, ok then. I will leave you alone. have a good life.')