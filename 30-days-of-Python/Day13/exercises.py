# Exercises: Day 13

# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positives = [n for n in numbers if n>0]
negatives = [n for n in numbers if n<1]
print(positives, negatives)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [number for biglist in list_of_lists for smalllist in biglist for number in smalllist]
print(flatten)

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Using list comprehension create the following list of tuples:
listoftuple = [(i, i**0, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(listoftuple)
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_codes = [(country.upper(), country[0:3].upper(), capital.upper()) for list in countries for country, capital in list]
print(country_codes)
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dicv = [{'country': country.upper(), 'city': city.upper()} for list in countries for country, city in list]
print(countries_dicv)
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]


# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_concat = [name + " " + surname for list in names for name, surname in list]
print(names_concat)
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1,y1,x2,y2: (y2-y1)/(x2-x1)
print(slope(-4,-8,2,2))
