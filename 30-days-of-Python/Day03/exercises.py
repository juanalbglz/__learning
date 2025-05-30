# TODO Exercises - Day 3

# [x] Declare your age as integer variable
my_age = 43
# [x] Declare your height as a float variable
my_height = 169.5
# [x] Declare a variable that store a complex number
my_complex_number = 10 + 3j

"""
[x] Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
"""
print("=== Calculate the area of a triangle ===")
base = int(input("Enter base: "))
height = int(input("Enter height: "))
print(f"The area of the triangle is {0.5 * base * height}")

""" 
[x] Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
    Enter side a: 5
    Enter side b: 4
    Enter side c: 3
    The perimeter of the triangle is 12
"""
print("=== Calculate the perimeter of a triangle ===")
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))
print(f"The perimeter of the triangle is {side_a + side_b + side_c}")

# [x] Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("=== Calculate area and perimeter of a rectangle ===")
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print(f"The area of the rectangle is {length * width} and it's perimeter is {2 * (length + width)}")

# [x] Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("=== Calculate area and circumference of a circle ===")
pi = 3.14
r = int(input("Enter radius: "))
print(f"The area of the circle is {pi * r ** 2} and it's perimeter is {2 * pi * r}")

# [x] Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_intercept = (0,2)
y_intercept = (1,0)
calculate_slop1 = (0-2)/(1-0)
print("The first slope is ",calculate_slop1)

# [x] Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
point_1 = (2,2)
point_2 = (6.10)
calculate_slop2 = (10-2)/(6-2)
print("The second slope is ", calculate_slop2)

# [x] Compare the slopes in tasks 8 and 9.
print("Compare the slopes: Are they equal? ", calculate_slop1 == calculate_slop2)
print("Compare the slopes: Is slope1 greater? ", calculate_slop1 > calculate_slop2)
print("Compare the slopes: Is slope2 greater? ", calculate_slop1 < calculate_slop2)

# [x] Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-10, 10):
    equation = x**2 + 6*x + 9
    print(f"x = {x}, equation = {equation}")
print(f"for x = -3, equation = {x**2 + 6*x + 9}")

# [x] Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") > len("dragon"))

# [x] Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("check if 'on' is found in both 'python' and 'dragon': ", "on" in "python" and "on" in "dragon")

# [x] I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("Check if jargon is in the sentence 'I hope this course is not full of jargon': ", "jargon" in "I hope this course is not full of jargon")

# [x] There is no 'on' in both dragon and python
print("There is no 'on' in both dragon and python: ", not("on" in "dragon" and "on" in "python"))

# [x] Find the length of the text python and convert the value to float and convert it to string
print("Length of 'python': ", len("python"), " casted to float: ", float(len("python")), " and casted to string: ", str(float(len("python"))))

# [X] Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print("=== Find if a number is even or odd via modulus (%) ===")
for x in range (1,20):
    if (x%2 > 0):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

# [x] Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print (f"Check if the floor division of 7 by 3 is equal to the int converted value of 2.7: {7//3 == int(2.7)}")

# [x] Check if type of '10' is equal to type of 10
print(f"Check if type of '10' is equal to type of 10 {type('10') == type(10)}")

# [x] Check if int('9.8') is equal to 10
print(f"Check if int('9.8') is equal to 10 {int(9.8) == 10}")

"""
[x] Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
    Enter hours: 40
    Enter rate per hour: 28
    Your weekly earning is 1120
"""
hours, rate = int(input("Enter hours: ")), int(input("Enter rate per hour: "))
print(f"Your weekly earning is {rate * hours}")

"""
[x] Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
    Enter number of years you have lived: 100
    You have lived for 3153600000 seconds.
"""
years = int(input("Enter number of years you have lived: "))
print(f"You have lived for {years*365*24*60*60} seconds")

"""
[ ] Write a Python script that displays the following table
    1 1 1 1 1
    2 1 2 4 8
    3 1 3 9 27
    4 1 4 16 64
    5 1 5 25 125
"""
for x in range(1,6):
    for y in range (-1, 4):
        print (x ** abs(y), end=" ")
    print()