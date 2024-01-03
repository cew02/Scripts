t = "Cody"

print(len(t) > 1 and t.count('n') < 4)

a = 32

print(a > 4 / 15 or a == 2 * 16)

# Assign some medium string
test = "medium string"

# Conditional statements
if len(test) > 20:
    print("String: '", test, "' is large")
elif len(test) > 10:
    print("String: '", test, "' is medium")
else:
    print("String: '", test, "' is small")
    
# One more checking
test = "small"

# Conditional statement
if len(test) > 20:
    print("String: '", test, "' is large")
elif len(test) > 10:
    print("String: '", test, "' is medium")
else:
    print("String: '", test, "' is small")