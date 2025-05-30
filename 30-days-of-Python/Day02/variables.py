# TODO Exercises: Level 1
# [x] Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# [x] Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming
# [x] Declare a first name variable and assign a value to it


first_name = "Juan Alberto"
# [x] Declare a last name variable and assign a value to it
last_name = "González"
# [x] Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
# [x] Declare a country variable and assign a value to it
country = "Canary Islands"
# [x] Declare a city variable and assign a value to it
city = "Tenerife"
# [x] Declare an age variable and assign a value to it
age = "43"
# [x] Declare a year variable and assign a value to it
year = 2022
# [x] Declare a variable is_married and assign a value to it
is_married = False
# [x] Declare a variable is_true and assign a value to it
is_true = False
# [x] Declare a variable is_light_on and assign a value to it
is_light_on = False
# [x] Declare multiple variable on one line
first_name, last_name, country, city, age, year, is_married, is_true, is_light_on = "Juan Alberto", "González", "Canary Islands", "Tenerife", "43", 2022, False, False, False


# TODO Exercises: Level 2
# [x] Check the data type of all your variables using type() built-in function
variables = [first_name, last_name, country, city, age, year, is_married, is_true, is_light_on]
for variable in variables:
    print(f'Type of {variable} is ', type(variable))

# [x] Using the len() built-in function, find the length of your first name
print(f'Length of {first_name} is ', len(first_name))
# [x] Compare the length of your first name and your last name
print(f'Length of {first_name} is {len(first_name)} and length of {last_name} is {len(last_name)}')
# [x] Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
# [x] Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
# [ ] Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
# [x] Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
# [x] Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
# [x] Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
# [x] Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
# [x] Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
# [x]The radius of a circle is 30 meters.
circle_radius = 30
pi = 3.1417
# [ ] Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * circle_radius ** 2
# [x] Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * circle_radius
# [x] Take radius as user input and calculate the area.
circle_radius = int(input("Circle radius: "))
area_of_circle = pi * circle_radius ** 2
print(f"Circle area: {area_of_circle}")
# [x] Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name, last_name, country, age = input("First Name: "), input("Last Name: "), input("Country: "), int(input("Age: "))
# [x]Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print(help('keywords'))