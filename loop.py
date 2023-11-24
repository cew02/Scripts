# While Loops



# Assign starting number (counter)
i = 1

# While loop will print all the numbers to 10
while i < 10: # Condition
  print(i, end = ' ') # Action
  i = i + 1 # Increasing variable


i = 1

while i < 10:
  print(i**2)
  i = i + 1

# For Loops

# For loops use strings

# Initial string
word = 'Saber'

# Initialize a for loop
for i in word:
  print(i, end = ' ')
# This block of code runs through the elements of the word "Saber"

# Lists

# Initial list
values = [1, [2, 3], 4, "code"]

# Initialize a for loop
for el in values:
  print(el, end = ' ')

# "el" is short for "elements". Can use "i" instead

people = ['Cody', 'Camron', 'Brian', 'Ceasar']

for i in people:
  print(i, end ='')

# Using range

for i in range(5):
  print(i, end = '')

# ex: if n = 5, the code prints from 0-4 but does not include n

# Two arguments, n and m

for i in range(5,10):
  print(i, end = '')

# This block prints the numbers 5-9

# 3 arguments, n m and s

for i in range(5, 10, 15):
  print(i, end = '')

# This block starts from n, ends before m, and adds by s

for i in range(10, 21):
  print(i**2)

# This block prints the range of 10-20 squared