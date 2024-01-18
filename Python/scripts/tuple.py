# tuple - basically the other list, without the brackets

# Create tuple
US_Info = ("USA", 9629091, 331002651)
print(type(US_Info))

# You can also use tuple()

# Adding new data

# Much like merging lists

# Initial tuple
places = ("Georgia", 30269, "West Virginia", 25801)

# New data
places_upd = ("New York", 10001, "California", 90001)

# Merge
new_places = places + places_upd
print(new_places)

# Tuples cannot extend

# Python index starts at 0 --> 1 --> 2

names = (("West Virginia", "Cody", "Alex", "Brian", "Camron"),("New York", "Brandon", "Henry", "Tio"))

print(names[1])
print(names[0][2])

locations = ("Chick-Fil_a", "Mcdonalds", "Taco Bell")

locations_new = ("Chipotle", "Qdoba", "Long John Silvers")
new_locations = locations + locations_new

print (new_locations)
print(locations[1])
print(locations_new[2])
# Remember, indexing the first thing is still 0, then 1


