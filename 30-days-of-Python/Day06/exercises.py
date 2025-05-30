# Exercises: Level 1
# Create an empty tuple


empty_tuple = tuple()
print(empty_tuple)
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('César', 'Jorge')
sisters = ('Patricia',)
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# How many siblings do you have?
print("len(siblings): ", len(siblings))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Juan Manuel', 'Micaela')
family_members = siblings + parents
print("family_members: ", family_members)
# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = family_members[0: -2]
parents = family_members[len(family_members)-2: len(family_members)]
print(siblings)
print(parents)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Eggs', 'Butter', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(len(food_stuff_lt))
print(food_stuff_lt[int(len(food_stuff_lt)/2)-1: int(len(food_stuff_lt)/2+1)])
# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[0:3]+food_stuff_lt[-3:])
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Estonia is nordic?: ", 'Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print("Iceland is nordic?: ", 'Iceland' in nordic_countries)
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')