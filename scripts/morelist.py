# more list stuff :-)

countries_2d = [['USA', 25901], ['Canada', 78392], ['Germany', 73829]]

print(countries_2d[2])
print(countries_2d[1][0])

people = [['Cody', 21], ['Camron', 21], ['Brandon', 30], ['Brian', 20]]

# Printing first person's name and age
print(people[0])

# Printing second person's age
print(people[1][1])

# Printing fourth person's name
print(people[3][0])

places = [['Georgia', 'Atlanta', 'Peachtree City'], ['California', 'Los Angeles', 'Hollywood'], ['New York', 'New York City', 'Broadway']]

print(places[2][2])

print(places[0][1])

print(places[1][2])

places_upd = [['West Virginia', 'Beckley', 'Crab Orchard'], ['Indiana', 'South Bend', 'Mishawaka']]

places.extend(places_upd)
print(places[4])