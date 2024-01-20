num = int(input("Please enter a number: "))

if (num % 2) == 0:
    print('{0} is even'.format(num))
else:
    print('{0} is odd'.format(num))

# .format is used to format strings
# .format(num) 
    
# example: 
    
string = "Hello, {}"
formatted_string = string.format('world') # you can replace "world" with any word and it will print that word.
print(formatted_string)