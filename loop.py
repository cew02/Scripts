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