# DAY 5 - Lists

lst = list() # this is an empty list, no item in the list
print("Length of an empty list: ", len(lst)) # 0

# La función list() genera una nueva lista vacía

print("\n\n")
empty_list = [] # this is an empty list, no item in the list
print("Length of an empty list: ", len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print("\n\n")
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
input("press a key")

# Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

print("\n\n")
print("Accessing list elements with positive indexes")
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print("First fruit: ", first_fruit)      # banana
second_fruit = fruits[1]
print("Second fruit: ", second_fruit)     # orange
last_fruit = fruits[3]
print("Last fruit: ", last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
input("press a key")

print("\n\n")
print("Accessing list element with negative indexes")
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print("First fruit [-4]: ", first_fruit)      # banana
print("Last fruit [-1]: ", last_fruit)       # lemon
print("Second last fruit [-2]: ]", second_last)      # mango
input("press a key")

print("\n\n")
print("Unpacking list items")
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(lst)
print("first_item, second_item, third_item, *rest = lst")
print("First item: ", first_item)     # item1
print("Second item: ", second_item)    # item2
print("Third item: ", third_item)     # item3
print("*rest", rest)           # ['item4', 'item5']
input("press a key")

print("\n\n")
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
input("press a key")

print("\n\n")
print("Slice elements from a list [startindex:lastindex:step]")
print("Either with positive indexes")
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
input("press a key")

print("\n\n")
print("Slice elements from a list [startindex(negative):lastindex(negative):step]")
print("Or with negative indexes")
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
print("We can reverse a list with [::-1]")
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
input("press a key")

print("\n\n")
print("Modify a list")
print("List is a mutable or modifiable ordered collection of items.")
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits)
print("Modifying index 0 with fruits[0] = 'avocado'")
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
print("Modifying index 1 with fruits[0] = 'apple'")
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
input("press a key")

print("\n\n")
print("Checking Items in a List")
print("Checking an item if it is a member of a list using in operator. See the example below.")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
does_exist = 'banana' in fruits
print("banana in fruits: ", does_exist)  # True
does_exist = 'lime' in fruits
print("lime in fruits: ", does_exist)  # False
input("press a key")

print("\n\n")
print("Adding Items to a List")
print("To add item to the end of an existing list we use the method append().")
# syntax
print("lst = list()")
lst = list()
print("lst.appent('item')")
lst.append("item")
print("lst: ", lst)
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
fruits.append('apple')
print("fruits.append('apple')")
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
print("fruits.appent('lime')")
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
input("press a key")

print("\n\n")
print("Inserting Items into a List")
print("We can use insert() method to insert a single item at a specified index in a list. \nNote that other items are shifted to the right. \nThe insert() methods takes two arguments:index and an item to insert.")
# syntax
lst = ['item1', 'item2']
print("lst.insert(index, item)")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
print("fruits.insert(2, 'apple')")
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print("fruits.insert(3, 'lime')")
print(fruits)
input("press a key")

print("\n\n")
print("Removing Items from a List")
print("The remove method removes a specified item from a list")
print("syntax")
print("lst = ['item1', 'item2']")
print("lst.remove(item)")
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print("fruits: ", fruits)
fruits.remove('banana')
print("fruits.remove('banana')")
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print("fruits.remove('lemon')")
print(fruits)  # ['orange', 'mango', 'banana']
input("press a key")

print("\n\n")
print("Removing Items Using Pop")
print("The pop() method removes the specified index, (or the last item if index is not specified)")
print("# syntax")
print("lst = ['item1', 'item2']")
print("lst.pop()       # last item")
print("lst.pop(index)")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
fruits.pop()
print("fruits.pop()")
print(fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print("fruits.pop(0)")
print(fruits)       # ['orange', 'mango']
input("press a key")

print("\n\n")
print("Removing Items Using Del")
print("The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely")
print("syntax")
print("lst = ['item1', 'item2']")
print("del lst[index] # only a single item")
print("del lst        # to delete the list completely")
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
print("fruits: ", fruits)
del fruits[0]
print("del fruits[0]")
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print("del fruits[1]")
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print("del fruits[1:3]")
print(fruits)       # ['orange', 'lime']
del fruits
print("del fruits")
print("print(fruits) throws an error  NameError: name 'fruits' is not defined")
input("press a key")

print("\n\n")
print("Clearing List Items")
print("The clear() method empties the list:")
print("syntax")
print("lst = ['item1', 'item2']")
print("lst.clear()")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
fruits.clear()
print("fruits.clear()")
print(fruits)       # []
input("press a key")


print("\n\n")
print("Copying a List")
print("""It is possible to copy a list by reassigning it to a new variable in the following way: 
list2 = list1. 
Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, 
list2. But there are lots of case in which we do not like to modify the original instead we like 
to have a different copy. One of way of avoiding the problem above is using copy().""")
print("syntax")
print("lst = ['item1', 'item2']")
print("lst_copy = lst.copy()")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
fruits_copy = fruits.copy()
print("fruits_copy = fruits.copy()")
print("fruits_copy: ", fruits_copy)
input("press a key")

print("\n\n")
print("Joining Lists")
print("There are several ways to join, or concatenate, two or more lists in Python.")
print("Plus Operator (+)")
print("syntax")
print("list3 = list1 + list2")
positive_numbers = [1, 2, 3, 4, 5]
print("positive_numbers: ", positive_numbers)
zero = [0]
print("zero: ", zero)
negative_numbers = [-5,-4,-3,-2,-1]
print("negative_numbers: ", negative_numbers)
integers = negative_numbers + zero + positive_numbers
print("integers = negative_numbers + zero + positive_numbers")
print("integers: ", integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print("vegetables: ", vegetables)
fruits_and_vegetables = fruits + vegetables
print("fruits_and_vegetables = fruits + vegetables")
print("fruits_and_vegetables: ", fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
input("press a key")

print("\n\n")
print("Joining using extend() method")
print("The extend() method allows to append list in a list. See the example below.")
print("syntax")
print("list1 = ['item1', 'item2']")
print("list2 = ['item3', 'item4', 'item5']")
print("list1.extend(list2)")
print("list1 = ['item1', 'item2','item3', 'item4', 'item5']")
num1 = [0, 1, 2, 3]
print("num1: ", num1)
num2= [4, 5, 6]
print("num2: ", num2)
num1.extend(num2)
print("num1.extend(num2)")
print('num1:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
print("negative numbers: ", negative_numbers)
positive_numbers = [1, 2, 3,4,5]
print("positive numbers: ", positive_numbers)
zero = [0]
print("zero: ", zero)
negative_numbers.extend(zero)
print("negative_numbers.extend(zero)")
negative_numbers.extend(positive_numbers)
print("negative_numbers.extend(positive_numbers)")
print('negative numbers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print("vegetables: ", vegetables)
fruits.extend(vegetables)
print("fruits.extend(vegetables)")
print('fruits:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
input("press a key")

print("\n\n")
print("Counting Items in a List")
print("The count() method returns the number of times an item appears in a list:")
print("syntax")
print("lst = ['item1', 'item2']")
print("lst.count(item)")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
print("fruits.count('orange'): ", fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("ages: ", ages)
print("ages.count(24)", ages.count(24))           # 3
input("press a key")

print("\n\n")
print("Finding Index of an Item")
print("The index() method returns the index of an item in the list:")
print("syntax")
print("lst = ['item1', 'item2']")
print("lst.index(item)")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
print("fruits.index('orange'): ", fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("ages: ", ages)
print("ages.index(24): ", ages.index(24))           # 2, the first occurrence
input("press a key")

print("\n\n")
print("Reversing a List")
print("The reverse() method reverses the order of a list.")
print("syntax")
print("lst = ['item1', 'item2']")
print("lst.reverse()")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
fruits.reverse()
print("fruits.reverse()")
print("fruits: ", fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("ages: ", ages)
ages.reverse()
print("ages.reverse()")
print("ages: ", ages) # [24, 25, 24, 26, 25, 24, 19, 22]
input("press a key")

print("\n\n")
print("Sorting List Items")
print("""To sort lists we can use sort() method or sorted() built-in functions. 
The sort() method reorders the list items in ascending order and modifies the original list. 
If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.""")
print("sort(): this method modifies the original list")
input("press a key")

print("syntax")
print("lst = ['item1', 'item2']")
print("lst.sort()                # ascending")
print("lst.sort(reverse=True)    # descending")
print("Example:")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
fruits.sort()
print("fruits.sort(): ", fruits)
# sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print("fruits.sort(reverse=True): ", fruits)
 # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("ages: ", ages)
ages.sort()
print("ages.sort(): ", ages)
ages.sort(reverse=True)
print("ages.sort(reverse=True): ", ages)
print("\n\n")
print("sorted(): returns the ordered list without modifying the original list Example:")
fruits = ['banana', 'orange', 'mango', 'lemon']
print("fruits: ", fruits)
print("sorted(fruits): ", sorted(fruits))
print("sorted(fruits, reverse= True): ", sorted(fruits, reverse=True))
print("fruits: ", fruits)     # ['orange', 'mango', 'lemon', 'banana']
input("press a key")