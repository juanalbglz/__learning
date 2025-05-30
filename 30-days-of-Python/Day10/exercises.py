# Exercises: Day 10
# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
print("Iterate 0 to 10 using for loop, do the same using while loop.")
print("for loop iteration in range(1,11)")
for x in range(0,11):
    print(x)
print("while loop x=1 , x < 11")
x = 0
while x < 11:
    print(x)
    x+=1

# Iterate 10 to 0 using for loop, do the same using while loop.
print("Iterate 10 to 0 using for loop, do the same using while loop.")
print("for loop x in range (10, 0, -1)")
for x in range(10, -1, -1):
    print(x)
print("while loop x = 10, x > -1 x-=1")
x = 10
while x > -1:
    print(x)
    x-=1
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for x in range(8):
    print(x*'#')
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# Use nested loops to create the following:
for x in range(8):
    for y in range(9):
        if y<8:
            print("#", end=' ')
        else:
            print("#")
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for x in range(11):
    print(f"{x} x {x} = {x**2}")
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for element in list:
    print(element)
# Use for loop to iterate from 0 to 100 and print only even numbers
print("even numbers 0-100")
for x in range(101):
    if x%2==0:
        print(x)
# Use for loop to iterate from 0 to 100 and print only odd numbers
print("odd numbers 0-100")
for x in range(101):
    if x%2==1:
        print(x)
# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for x in range(101):
    sum+=x
print(sum)
# The sum of all numbers is 5050.
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_odd = 0
sum_even = 0
for x in range(101):
    if x%2==0:
        sum_even += x
    else:
        sum_odd += x
print("Evens sum: ", sum_even)
print("Odds sum: ", sum_odd)
print("Total: ", sum_even+sum_odd)
# The sum of all evens is 2550. And the sum of all odds is 2500.
# Exercises: Level 3

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop")
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for x in range ((len(fruits)-1),-1,-1):
    reversed_fruits.append(fruits[x])
print(reversed_fruits)
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world