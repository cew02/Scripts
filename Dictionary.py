# Create dictionary
countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
            'Germany': (357114, 83783942)}

print(countries_dict)

# Dictionaries are closed with curly brackets {}
# Immunitable means cannot be modified

# To take particular things from a dictionary

countries_dict = {'USA': (9629091, 331002651), 'Canada': (9984670, 37742154), 
            'Germany': (357114, 83783942)}

print(countries_dict['USA'])
# This takes the size of the USA: 9629091, and the apporximate population (as of 2020)

# My own

people = {'Cody': (21, 163), 'Camron': (21, 193)}
print(people['Camron'])

# Updating dictionary with new data

# len(d) - returns the number of key:value pairs in the dictionary d.
# d.copy() - creates a copy of the dictionary d.
# d.items() - provides all the key, value pairs from the dictionary d.
# d.keys() - lists all the keys in the dictionary d.
# d.values() - provides all the values from the dictionary d.

people = {'Daniel': (23, 146), 'Alex': (49, 80)}

# updating dictionary with two more people

people['James'] = (32 , 150)
people['Andrew'] = (18, 200)

print(people)