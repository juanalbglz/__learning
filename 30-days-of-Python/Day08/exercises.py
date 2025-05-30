# Create an empty dictionary called dog
print("Create an empty dictionary called dog")
dog = {}
print("dog = {}")
print("dog: ", dog)
# Add name, color, breed, legs, age to the dog dictionary
print("Add name, color, breed, legs, age to the dog dictionary:\ndic['key'] = 'value' \nOR \ndict = {\n\t'key':'value',\n\t'key2':'value2'\n\t}")
# dog['color'] = 'color'
# dog['breed'] = 'breed'
# dog['legs'] = 'legs'
# dog['age'] =  'age'
dog = {
    'color':'color',
    'breed':'breed',
    'legs':'legs',
    'age':'age',
    }
print("dog.keys(): ", dog.keys())
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
print("Create a student dictionary and add following keys: \nfirst_name, \nlast_name, \ngender, \nage, \nmarital status, \nskills, \ncountry, \ncity and \naddress")
student = {
    'first_name' : 'First Name',
    'last_name' : 'Last Name',
    'gender' : 'Gender',
    'age' : 'Age',
    'marital_status': 'Marital_status',
    'skills': 'Skills',
    'country': 'Country',
    'city':'City',
    }
print("student dictionary: ", student)
# Get the length of the student dictionary
print("Get the length of the student dictionary")
print("len(student): ", len(student))
# Get the value of skills and check the data type, it should be a list
print("Get the value of skills and check the data type, it should be a list")
print("len(student['skills']: ", len(student['skills']))
print("type(student['skills']): ", type(student['skills']))
print("student['skills'] = list(student['skills'])")
student['skills'] = list(student['skills'])
print("len(student['skills']: ", len(student['skills']))
print("type(student['skills']): ", type(student['skills']))
# Modify the skills values by adding one or two skills
print("Modify the skills values by adding one or two skills")
print("student['skills'].append('those')")
student['skills'].append('those')
print("len(student['skills']: ", len(student['skills']))
print("type(student['skills']): ", type(student['skills']))
# Get the dictionary keys as a list
print("Get the dictionary keys as a list")
print("student.keys(): ", student.keys())
print("type(student.keys()): ", type(student.keys()))
print("list(student.keys()): ", list(student.keys()))
print("type(list(student.keys())): ", type(list(student.keys())))
# Get the dictionary values as a list
print("Get the dictionary values as a list")
print("student.values(): ", student.values())
print("type(student.values()): ", type(student.values()))
print("list(student.values()): ", list(student.values()))
print("type(list(student.values())): ", type(list(student.values())))
# Change the dictionary to a list of tuples using items() method
print("Change the dictionary to a list of tuples using items() method")
print("student.items(): ", student.items())
# Delete one of the items in the dictionary
print("Delete one of the items in the dictionary")
print("Get the length of the student dictionary")
print("len(student): ", len(student))
print("student.popitem()", student.popitem())
print("Get the length of the student dictionary")
print("len(student): ", len(student))
# Delete one of the dictionaries
print("Delete one of the dictionaries")
print("del student: ")
del student
print("student: NameError: name 'student' is not defined")