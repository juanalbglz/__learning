# Exercises: Day 5
# Exercises: Level 1
# Declare an empty list
from yaml import scan


lst = list()
lst = []
# Declare a list with more than 5 items
lst = [1, 2, 3, 4, 5, 6, 7]
print("lst: ", lst)
#Find the length of your list
print("len(lst): ", len(lst))
#Get the first item, the middle item and the last item of the list
print("First item lst[0]: ", lst[0])
print("Last item lst[-1]: ", lst[-1])
print("Middle item lst[int(len(lst)/2)]", lst[int(len(lst)/2)])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Juan Alberto", 43, 170, "single", "Fasnia"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print("it_companies: ", it_companies)
# Print the number of companies in the list
print("len(it_companies): ", len(it_companies))
# Print the first, middle and last company
print("1st IT Company it_companies[0]: ", it_companies[0])
print("last IT Company it_companies[-1]: ", it_companies[-1])
print("Middle IT Company it_companies[int(len(it_companies)/2)]: ", it_companies[int(len(it_companies)/2)])
# Print the list after modifying one of the companies
print("Setting 1st element to Adobe it_companies[0]=\"Adobe\"")
it_companies[0]="Adobe"
print("it_companies: ", it_companies)
# Add an IT company to it_companies
print("Add Facebook it_companies.append(\"Facebook\")")
it_companies.append("Facebook")
# Insert an IT company in the middle of the companies list
print("Insert Paypal in the middle of the list. it_companies.insert(int(len(it_companies)/2), 'Paypal')")
it_companies.insert(int(len(it_companies)/2), 'Paypal')
print("it_companies: ", it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
print("Change Adobe to capital letters it_companies[0] = it_companies[0].upper()")
it_companies[0] = it_companies[0].upper()
print("it_companies: ", it_companies)
# Join the it_companies with a string '#;  '
print("Join the it_companies with the string '#;  '")
print("it_companies.extend('#;  ')")
it_companies.extend('#;  ')
print("it_companies: ", it_companies)
# Check if a certain company exists in the it_companies list.
print("ADOBE in it_companies?: ", 'ADOBE' in it_companies)
# Sort the list using sort() method
print("Sort the list with the sort method")
it_companies.sort()
print("it_companies: ", it_companies)
# Reverse the list in descending order using reverse() method
print("Reverse the lit with the reverse() method")
it_companies.reverse()
print("it_companies: ", it_companies)
# Slice out the first 3 companies from the list
print("Slice out the first 3 companies")
print("it_companies[0:3]", it_companies[0:3])
# Slice out the last 3 companies from the list
print("Slice out the last 3 companies")
print("it_companies[-3:]", it_companies[-3:])
# Slice out the middle IT company or companies from the list
print("Slice out the middle IT company")
print(it_companies[int(len(it_companies)/2)])
# Remove the first IT company from the list
print("Remove the first IT company from the list del it_companies[0]")
del it_companies[0]
print("it_companies: ", it_companies)
# Remove the middle IT company or companies from the list
print("Remove the middle IT company or companies from the list")
print("lenght of it_companies: ", len(it_companies)) #12
del it_companies[int(len(it_companies)/2)-1:(int(len(it_companies)/2)+1) ]
print("it_companies without middle elements: ", it_companies)
# Remove the last IT company from the list
print("Remove the last IT company from the list it_companies.pop()")
it_companies.pop()
print("it_companies: ", it_companies)
# Remove all IT companies from the list
print("Remove all IT companies from the list it_companies.clear()")
it_companies.clear()
print("it_companies: ", it_companies)
# Destroy the IT companies list
print("Destroy the IT companies list del it_companies")
del it_companies
# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
print("front_end: ", front_end)
back_end = ['Node','Express', 'MongoDB']
print("back_end: ", back_end)
front_end.extend(back_end)
print("front_end: ", front_end)
full_stack = front_end.copy()
print("full_stack: ", full_stack)
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print("full_stack after insert new elements: ", full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("ages: ", ages)
print("Sort the list and find the min and max age")
print("sorted(ages): ", sorted(ages))
print("ages: ", ages)
print("min(ages)=sorted(ages)[0]: ", sorted(ages)[0], " max(ages)=sorted(ages)[-1] ", sorted(ages)[-1])
# Sort the list and find the min and max age
# Add the min age and the max age again to the list
print("Add the min age and the max age again to the list")
print("ages.append(sorted(ages)[0])")
ages.append(sorted(ages)[0])
print("ages.append(sorted(ages)[-1])")
ages.append(sorted(ages)[-1])
# Find the median age (one middle item or two middle items divided by two)
print("len(ages): ", len(ages))
print("sorted(ages): ", sorted(ages))
print("sorted(ages)[int(len(ages)/2)-1]: ", sorted(ages)[int(len(ages)/2)-1])
print("sorted(ages)[int(len(ages)/2)]: ", sorted(ages)[int(len(ages)/2)])
print("median = (sorted(ages)[6]+sorted(ages)[7])/2", ((sorted(ages)[6]+sorted(ages)[7])/2))
# Find the average age (sum of all items divided by their number )
print("Average sum: ", sum(ages)/len(ages))
# Find the range of the ages (max minus min)
print("Range = sorted(ages)[-1]-sorted(ages)[0]: ", sorted(ages)[-1]-sorted(ages)[0])
# Compare the value of (min - average) and (max - average), use abs() method
print("Compare the value of min - average using abs abs(sorted(ages)[0]-sum(ages)/len(ages)): ", abs(sorted(ages)[0]-sum(ages)/len(ages)))
print("Compare the value of max - average using abs abs(sorted(ages)[-1]-sum(ages)/len(ages)): ", abs(sorted(ages)[-1]-sum(ages)/len(ages)))
# Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("countries: ", countries)
print("len(countries): ", len(countries))
print("Middle country = countries[int(len(countries)/2).1]: ", countries[int(len(countries)/2)])
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print("Divide the countries list into two equal lists if it's even if not one more country on the first half")
print("len(countries)= 7, odd")
print("First half 0-4: ", countries[0:4])
print("Second half 4-7: ", countries[4:])
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
print("Unpack the first three countries and the rest as scandic countries")
first, second, third, *scandic = countries
print(scandic)