#  Exercises - Day 4

import os
day = 4

def print_statement(n,s):
    os.system('clear')
    print(f"\n\nDay {day} - Exercise {n}\n=== === === === === ===\nStatement: {s}\n")

def break_it():
    input("\n\nPress Enter to continue...")

# [x]Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
exercise = 1
exercise_statement = "Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'."
print_statement(exercise, exercise_statement)
strings = ("Thirty", "Days", "Of", "Python")
space = " "
concatenated = strings[0] + space + strings[1] + space + strings[2] + space + strings[3]
print(f"Concatenated string of {strings} is \"{concatenated}\" and it's length is {len(concatenated)}")
break_it()

# [x] Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
exercise = 2
exercise_statement = "Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'."
print_statement(exercise, exercise_statement)
strings = ('Coding', 'For' , 'All')
concatenated = strings[0] + space + strings[1] + space + strings[2]
print(f"Concatenated string of {strings} is \"{concatenated}\"")
break_it()

# [x] Declare a variable named company and assign it to an initial value "Coding For All".
exercise = 3
exercise_statement = "Declare a variable named company and assign it to an initial value \"Coding For All\"."
print_statement(exercise, exercise_statement)
company = "Coding For All"
print(f"Assigned value \"{company}\" to variable 'company'")
break_it()

# [x] Print the variable company using print().
exercise = 4
exercise_statement = "Print the variable company using print()."
print_statement(exercise, exercise_statement)
print(f"Company name: {company}")
break_it()

# [x] Print the length of the company string using len() method and print().
exercise = 5
exercise_statement = "Print the length of the company string using len() method and print()."
print_statement(exercise, exercise_statement)
print(f"Company name length: {len(company)}")
break_it()

# [x] Change all the characters to uppercase letters using upper() method.
exercise = 6
exercise_statement = "Change all the characters to uppercase letters using upper() method."
print_statement(exercise, exercise_statement)
print(f"company.upper(): {company.upper()}")
break_it()

# [x] Change all the characters to lowercase letters using lower() method.
exercise = 7
exercise_statement = "Change all the characters to lowercase letters using lower() method."
print_statement(exercise, exercise_statement)
print(f"company.lower(): {company.lower()}")
break_it()

# [x] Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
exercise = 8
exercise_statement = "Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All."
print_statement(exercise, exercise_statement)
print(f"company.capitalize(): {company.capitalize()}")
print(f"company.title(): {company.title()}")
print(f"company.swapcase(): {company.swapcase()}")
break_it()

# [x] Cut(slice) out the first word of Coding For All string.
exercise = 9
exercise_statement = "Cut(slice) out the first word of Coding For All string."
print_statement(exercise, exercise_statement)
first_word_out = company[company.find(' ')+1:]
print("I used the \033[1m find() \033[0m method to get the first space on the string")
print("Then I cut the first word out by using the position of the first space + 1")
print("\033[1mcompany[company.find(' ')+1:]\033[0m and the result is:",end=" ")
print(first_word_out)
break_it()

# [x] Check if Coding For All string contains a word Coding using the method index, find or other methods.
exercise = 10
exercise_statement = "Check if Coding For All string contains a word Coding using the method index, find or other methods."
print_statement(exercise, exercise_statement)
finder = "Coding"
if company.count(finder)>0:
    print(f"{finder} appears {company.count(finder)} in {company}")
    print(f"{finder} appears in {company} at position {company.index(finder)} using \033[1m index() \033[0m method")
    print(f"{finder} appears in {company} at position {company.find(finder)} using \033[1m find() \033[0m method")
break_it()

# [x] Replace the word coding in the string 'Coding For All' to Python.
exercise = 11
exercise_statement = "Replace the word coding in the string 'Coding For All' to Python."
print_statement(exercise, exercise_statement)
print("Using the method \033[1mreplace(old_str, new_str)\033[0m")
print('python_company = company.replace("Coding", "Python")')
python_company = company.replace("Coding", "Python")
print("And the result is: ", end="")
print(python_company)
break_it()

# [x] Change Python for Everyone to Python for All using the replace method or other methods.
exercise = 12
exercise_statement = "Change Python for Everyone to Python for All using the replace method or other methods."
print_statement(exercise, exercise_statement)
text = "Python for Everyone"
print(text)
print('python_company.replace("Everyone", "All"): ', end="")
print(python_company.replace("Everyone", "All"))
break_it()

# [x] Split the string 'Coding For All' using space as the separator (split()) .
exercise = 13
exercise_statement = "Split the string 'Coding For All' using space as the separator (split()) ."
print_statement(exercise, exercise_statement)
print('company.split(" ") throws following result: ', end="")
print(company.split(" "))
break_it()

# [x] "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
exercise = 14
exercise_statement = "\"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon\" split the string at the comma."
print_statement(exercise, exercise_statement)
big_internet = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Created a string 'big_internet' with the contents: ", big_internet)
print("Splitting with the method big_internet.split(", ") gives following result: ", end="")
print(big_internet.split(", "))
break_it()

# [x] What is the character at index 0 in the string Coding For All.
exercise = 15
exercise_statement = "What is the character at index 0 in the string Coding For All."
print_statement(exercise, exercise_statement)
print(f"First character in the string {company} with company[0] is {company[0]}")
break_it()

# [x] What is the last index of the string Coding For All.
exercise = 16
exercise_statement = "What is the last index of the string Coding For All."
print_statement(exercise, exercise_statement)
print(f"Last character of {company} with company[-1] is {company[-1]}")
break_it()

# [x] What character is at index 10 in "Coding For All" string.
exercise = 17
exercise_statement = "What character is at index 10 in \"Coding For All\" string."
print_statement(exercise, exercise_statement)
print(f"Character at index 10 of {company} with company[10] is {company[10]}")
break_it()

# [x] Create an acronym or an abbreviation for the name 'Python For Everyone'.
exercise = 18
exercise_statement = "Create an acronym or an abbreviation for the name 'Python For Everyone'."
print_statement(exercise, exercise_statement)
string = 'Python For Everyone'
print(f"Define a string with the text: string = {string}")
acronym = ""
print("Define a new variable to hold the acronym")
print("define a loop for char in string, and if it's upper add it to the acronym variable")
for char in string:
    print(f"Analyzing char {char} ...")
    if char.isupper():
        print(f"Char {char} is uppercase, adding to the acronym variable")
        acronym += char
print(f"Acronym of {string} is {acronym}")
break_it()

# [x] Create an acronym or an abbreviation for the name 'Coding For All'.
exercise = 19
exercise_statement = "Create an acronym or an abbreviation for the name 'Coding For All'."
print_statement(exercise, exercise_statement)
string = 'Coding For All'
print(f"Define a string with the text: string = {string}")
acronym = ""
print("Define a new variable to hold the acronym")
print("define a loop for char in string, and if it's upper add it to the acronym variable")
for char in string:
    print(f"Analyzing char {char} ...")
    if char.isupper():
        print(f"Char {char} is uppercase, adding to the acronym variable")
        acronym += char
print(f"Acronym of {string} is {acronym}")
break_it()

# [x] Use index to determine the position of the first occurrence of C in Coding For All.
exercise = 20
exercise_statement = "Use index to determine the position of the first occurrence of C in Coding For All."
print_statement(exercise, exercise_statement)
print(f"First 'C' char is found with string.index('C') at position {string.index('C')} in string \"{string}\"")
break_it()

# [x] Use index to determine the position of the first occurrence of F in Coding For All.
exercise = 21
exercise_statement = "Use index to determine the position of the first occurrence of F in Coding For All."
print_statement(exercise, exercise_statement)
print(f"First 'F' char is found with string.index('F') at position {string.index('F')} in string \"{string}\"")
break_it()

# [x] Use rfind to determine the position of the last occurrence of l in Coding For All People.
exercise = 22
exercise_statement = "Use rfind to determine the position of the last occurrence of l in Coding For All People."
print_statement(exercise, exercise_statement)
string = "Coding For All People"
print(f"Last 'l' char is found at position {string.rfind('l')} in string \"{string}\" with method string.rfind('l')")
break_it()

# [x] Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
exercise = 23
exercise_statement = "Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:\n 'You cannot end a sentence with because because because is a conjunction'"
print_statement(exercise, exercise_statement)
string = 'You cannot end a sentence with because because because is a conjunction'
search_for = 'because'
print(f"First occurrence of {search_for} is found at position {string.find(search_for)} with method string.find('because')")
break_it()

# [x] Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
exercise = 24
exercise_statement = "Use rindex to find the position of the last occurrence of the word because in the following sentence: \n'You cannot end a sentence with because because because is a conjunction'"
print_statement(exercise, exercise_statement)
print(f"Last occurrence of {search_for} is found at position {string.rfind(search_for)} with method string.rfind('because')")
break_it()

# [x] Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
exercise = 25
exercise_statement = "Slice out the phrase 'because because because' \nin the following sentence: \n'You cannot end a sentence with because because because is a conjunction'"
print_statement(exercise, exercise_statement)
string = 'You cannot end a sentence with because because because is a conjunction'
slice = 'because because because'
new_string = string.replace(slice,"")
print(f"The string after slicing out the substring with method string.replace({slice},\"\") is\n {new_string}")
break_it()

# [x] Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
exercise = 26
exercise_statement = "Find the position of the first occurrence of the word 'because' in the following sentence: \n'You cannot end a sentence with because because because is a conjunction'"
print_statement(exercise, exercise_statement)
print(f"First occurrence of {search_for} is found at position {string.find(search_for)} with method string.find('because')")
break_it()

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
exercise = 27
exercise_statement = "Find the position of the first occurrence of the word 'because' in the following sentence: \n'You cannot end a sentence with because because because is a conjunction'"
print_statement(exercise, exercise_statement)
print("This exercise is repeated as in exercise 25")
break_it()

# Does ''Coding For All' start with a substring Coding?
exercise = 28
exercise_statement = "Does ''Coding For All' start with a substring Coding?"
print_statement(exercise, exercise_statement)
print("Is is True that the sentence 'Coding For All' starts with the substring 'Coding'?", 'Coding for all'.startswith('Coding'))
print("Method applied: 'Coding for all'.startswith('Coding')")
break_it()

# Does 'Coding For All' end with a substring coding?
exercise = 29
exercise_statement = "Does 'Coding For All' end with a substring coding?"
print_statement(exercise, exercise_statement)
print("Is is True that the string 'Coding For All' ends with the substring 'Coding'?", 'Coding for all'.endswith('coding'))
print("Method applied: 'Coding for all'.endswith('coding')")
break_it()

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
exercise = 30
exercise_statement = "'   Coding For All      '  , remove the left and right trailing spaces in the given string."
print_statement(exercise, exercise_statement)
print("To trim whitespaces we can use the string method strip.")
print("We can apply is with string.strip('   Coding For All      ')")
print(string.strip('   Coding For All      '))
break_it()

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
exercise = 31
exercise_statement = "Which one of the following variables return True when we use the method isidentifier():\n\t30DaysOfPython\n\tthirty_days_of_python"
print_statement(exercise, exercise_statement)
print("Is '30DaysOfPython' a valid identifier?: ", '30DaysOfPython'.isidentifier())
print("Is 'thirty_days_of_python' a valid identifier?: ", 'thirty_days_of_python'.isidentifier())
print("To check if a string is a valid variable identifier we use 'var_name_to_check'.isidentifier()")
break_it()

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
exercise = 32
exercise_statement = "The following list contains the names of some of python libraries: \n['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. \nJoin the list with a hash with space string."
print_statement(exercise, exercise_statement)
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'] 
print(python_libraries, "Python Libraries as an array")
libraries_string = ""
print("Create a new string to contain the elements of the string separated by a space")
print("Create a for loop for each element in the array, add it to the string and append a space")
for library in python_libraries:
    libraries_string += library
    libraries_string += " "
print("Strip the string to take the last space out")
print(libraries_string)
libraries_string=string.strip(libraries_string)
print(libraries_string)
break_it()

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
exercise = 33
exercise_statement = """Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next."""
print_statement(exercise, exercise_statement)
print("""Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.""")
break_it()

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
exercise = 34
exercise_statement = """Use a tab escape sequence to write the following lines.
Name\t\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki"""
print_statement(exercise, exercise_statement)
print("""Use a tab escape sequence to write the following lines.
Name\tAge\tCountry\tCity
Asabeneh\t250\tFinland\tHelsinki""")
break_it()

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
exercise = 35
exercise_statement = """Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""
print_statement(exercise, exercise_statement)
radius = 10
print(f"radius = {radius}")
area = 3.14 * radius ** 2
print(f"area = 3.14 * radius ** 2")
print(f"The area of a circle with radius {radius} is {area} square meters")
break_it()

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
exercise = 36
exercise_statement = """Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""
print_statement(exercise, exercise_statement)
number_one = 8
number_two = 6
print(f"{number_one} + {number_two} = {number_one + number_two}")
print(f"{number_one} - {number_two} = {number_one - number_two}")
print(f"{number_one} * {number_two} = {number_one * number_two}")
print(f"{number_one} / {number_two} = {number_one / number_two}")
print(f"{number_one} % {number_two} = {number_one % number_two}")
print(f"{number_one} // {number_two} = {number_one // number_two}")
print(f"{number_one} ** {number_two} = {number_one ** number_two}")
break_it()