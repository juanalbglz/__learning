# Exercises: Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print("Find the length of the set it_companies")
print("len(it_companies): ", len(it_companies))
# Add 'Twitter' to it_companies
print("Add 'Twitter' to it_companies")
print("it_companies.add('Twitter')")
it_companies.add('Twitter')
print("it_companies: ", it_companies)
# Insert multiple IT companies at once to the set it_companies
print("Insert multiple IT companies at once to the set it_companies")
print("it_companies.update(['Canva', 'Netflix', 'Alphabet'])")
it_companies.update(['Canva', 'Netflix', 'Alphabet'])
print("it_companies: ", it_companies)
# Remove one of the companies from the set it_companies
print("Remove one of the companies from the set it_companies")
print("it_companies.remove('Google')")
it_companies.remove('Google')
print("it_companies: ", it_companies)
# What is the difference between remove and discard
print("What is the difference between remove and discard")
print("remove() raise an error if not fount while discard won't")
# Exercises: Level 2
# Join A and B
print("Join A and B")
print("A: ", A)
print("B: ", B)
print("A join B A.union(B): ", A.union(B))
# Find A intersection B
print("A intersection B A.intersection(B): ", A.intersection(B))
# Is A subset of B
print("A subset of B?: ", A.issubset(B))
# Are A and B disjoint sets
print("Are A and B disjoint sets?: ", A.isdisjoint(B))
# Join A with B and B with A
print("Join A with B and B with A")
print("Set unions are the same on each direction, all elements")
print("A.union(B), B.union(A): ", A.union(B))
# What is the symmetric difference between A and B
print("What is the symmetric difference between A and B")
print("A.symmetric_difference(B): ", A.symmetric_difference(B))
# Delete the sets completely
print("Delete the sets completely")
del A
del B
print("del A\ndel B")

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print("Convert the ages to a set and compare the length of the list and the set, which one is bigger")
age_st = set(age)
print("Compare lengths. Are they equal?", len(age)==len(age_st))
print("age list length: ", len(age))
print("age set length: ", len(age_st))
# Explain the difference between the following data types: string, list, tuple and set
print("string: collection of chars, non-mutable, iterable")
print("list: collection of different data types, mutable")
print("tuple: collection of different elements, unmutable")
print("set: collection of unique elements")
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
print("""I am a teacher and I love to inspire and teach people. 
How many unique words have been used in the sentence? 
Use the split methods and set to get the unique words.""")
str = "I am a teacher and I love to inspire and teach people"
print("str: " , str)

str_lst = list(str.split(" "))
str_st = set(str.split(" "))
print("len(str_lst): ", len(str_lst))
print("str_st = set(str.split(" "))")
print(str_st)
print("len(str_st): ", len(str_st))