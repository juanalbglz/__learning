# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.


age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18-age} more {'years' if (18-age)>1 else 'year'} to learn to drive.")
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 43
print(f"You are {abs(age-my_age)} {'years' if abs(18-age)>1 else 'year'} {'older' if age>my_age else 'younger'} than me")
# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print(f"number one {number_one} is greater than number two {number_two}")
elif number_two > number_one:
    print(f"number one {number_one} is smaller than number two {number_two}")
else:
    print(f"number one {number_one} is equal to number two {number_two}")

# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
punctuation = int(input("What is your punctuation: "))
if punctuation < 50:
    grade = 'F'
elif punctuation < 60:
    grade = 'D'
elif punctuation < 70:
    grade = 'C'
elif punctuation < 90:
    grade = 'B'
else:
    grade = 'A'
print(f"Your grade is {grade}")
# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autumn = {'September', 'October', 'November'}
winter = {'December', 'January', 'February'}
spring = {'March', 'April', 'April'}
summer = {'June', 'July', 'August'}
month = input("What month?: ")
if month in autumn:
    season = 'Autumn'
elif month in winter:
    season = 'Winter'
elif month in spring:
    season = 'Spring'
else:
    season = 'Summer'
print(f"This month belongs to the {season} season")

# The following list contains some fruits:

# fruits = ['banana', 'orange', 'mango', 'lprint(f"Skills {'found' if 'skills' in person.keys() else 'not found'}")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Fruit name: ")
if fruit in fruits:
    print(f"That fruit \"{fruit}\" already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)
# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!

# person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print("Checking skills")
if 'skills' in person.keys():
    print(person['skills'][int((len(person['skills'])-1)/2)])
    print("Python in person['skills']:", 'Python' in person['skills'])
    if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("Backend developer profile")
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("Fullstack developer profile")
    elif 'Javascript' in person['skills'] and 'React' in person['skills']:
        print("Frontend developer profile")
    else:
        print("Unknown profile")
else:
    print("No skills available")

#  * If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}")