names = ["Cody", "Alex", "Peerson", "Mike"]
new_names = ["Brian", "George"]

names_upd = names + new_names

names.extend(names)
print(names_upd)

countries_2d = [['USA', 25901], ['Canada', 78392], ['Germany', 73829]]

print(countries_2d[2])
print(countries_2d[1][0])

people = [["Alex", 23], ["Noah", 34], ["Peter", 29], ["John", 41], ["Michelle", 35]]

# Task 1: information about the fourth person
print(people[3])

# Task 2: name of the first person
print(people[0][0])

# Task 3: age of the fifth person
print(people[4][1])