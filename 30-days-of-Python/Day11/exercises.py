# Exercises: Day 11
# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a+b
print(add_two_numbers(3,4))
# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(r):
    return 3.14 * r ** 2
print(circle_area(10))
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. 
def add_all_nums(*nums):
    right_type = True
    for num in nums:
        if type(num) != int:
            right_type = False
            return "Nums must be integers"
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(1,2,3,4,5))
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(temp):
    return (temp * 9/5)+32
print(convert_celsius_to_fahrenheit(30))
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    months = ('september', 'october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august')
    if month in months:
        if months.index(month)<3:
            return 'Autumn'
        elif months.index(month)<6:
            return 'Winter'
        elif months.index(month)<9:
            return 'Spring'
        else:
            return 'Summer'
    else:
        return 'Not a valid month'
# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2, y2):
    return y2-y1/x2-x1
print(calculate_slope(1,1,4,4))
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    if a != 0:
        solution1 = (-b -(b**2 -4*a*c)**1/2)/2*a
        solution2 = (-b +(b**2 -4*a*c)**1/2)/2*a
        return (solution1, solution2)
    else:
        return (-c/b)
print(solve_quadratic_eqn(0,10,-2))
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for element in lst:
        print(element)
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    lst2 = list()
    while len(lst)>0:
        lst2.append(lst.pop())
    return lst2
print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# # ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    n = 0
    while n < len(lst):
        lst[n] = lst[n].capitalize()
        n+=1
    return lst
print(capitalize_list_items(['one', 'two']))
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item([1,2,3],4))
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.pop(lst.index(item))
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for x in range (num+1):
        sum += x
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for x in range (num+1):
        if x%2==1:
            sum += x
    return sum
print(sum_of_odds(5))  # 9
print(sum_of_odds(10)) # 25
print(sum_of_odds(100)) # 2500
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    sum = 0
    for x in range (num+1):
        if x%2==0:
            sum += x
    return sum
print(sum_of_even(5))  # 6
print(sum_of_even(10)) # 30
print(sum_of_even(100)) # 2550
# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
def evens_and_odds(n):
    evens = 0
    odds = 0
    for x in range (abs(n)):
        if x%2==0:
            evens += 1
        else:
            odds += 1
    print(f"The number of odds is {odds}\nThe number of evens is {evens}")
evens_and_odds(5)
evens_and_odds(1)
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    fact = 1
    for x in range(1,n):
        fact *= n
    return fact
print(factorial(2))
print(factorial(5))
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(obj):
    return bool(obj)
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst): #average value
    return sum(lst)/len(lst)

def calculate_median(lst): #value in the middle of the list
    slst = sorted(lst)
    if (len(slst))%2==0:
        return (slst[(int((len(slst)-1)/2))] + slst[(int((len(slst)-1)/2)+1)])/2
    else:
        return slst[(int((len(slst))/2))]

def calculate_mode(lst):
    lst_set = set(lst)
    lst_dic = dict.fromkeys(lst_set, 0)
    for element in lst:
        lst_dic[element] = lst_dic[element]+1
    lst_dic_val = lst_dic.values()
    if len(lst)-1 == sum(lst_dic_val):
        return f"No repeating item, no mode for the list {lst}"
    else:
        return max(lst_dic, key=lst_dic.get)

def calculate_range(lst):
    return (min(lst), max(lst))

def calculate_variance(lst):
    median = calculate_median(lst)
    median_lst = list()
    for element in lst:
        median_lst.append((element-median)**2)
    return sum(median_lst)/len(median_lst)
    
def calculate_std(lst):
    return(calculate_variance(lst))**0.5
print(calculate_std([1,3,2,20,20])) 

# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    n = abs(int(n))
    divisors = list()
    for x in range(1,n+1):
        if n%x==0:
            divisors.append(x)
    if len(divisors)>2:
        return False
    else:
        return True

# Write a functions which checks if all items are unique in the list.
def all_unique(lst):
    lst_st = set(lst)
    if len(lst)== len(lst_st):
        return True
    else:
        return False

# Write a function which checks if all the items of the list are of the same data type.
def all_same_type(lst):
    type_zero = type(lst[0])
    for element in lst:
        if type(element) != type_zero:
            return False
    return True

# Write a function which check if provided variable is a valid python variable
def valid_variable(str):
    return str.isidentifier()

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.