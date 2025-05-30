# Day 1 - 30DaysOfPython Challenge

from platform import python_version


print("Addition (+): 2 + 3 = ", 2 + 3)             # addition(+)
print("Substraction (-): 3 - 1 = ", 3 - 1)             # subtraction(-)
print("Multiplication (*): 2 * 3 = ", 2 * 3)             # multiplication(*)
print("Division (/): 3 / 2 = ", 3 / 2)             # division(/)
print("Exponent (**): 3 ** 2 = ", 3 ** 2)            # exponential(**)
print("Modulus (%): 3 % 2 = ", 3 % 2)             # modulus(%)
print("Floor division operator (//): 3 // 2 = ", 3 // 2)            # Floor division operator(//)

# Checking data types
print("type(10) = ",type(10))          # Int
print("type(3.14) = ",type(3.14))        # Float
print("type(1 + 3j) = ",type(1 + 3j))      # Complex number
print("type('Asabeneh') = ",type('Asabeneh'))  # String
print("type([1, 2, 3]) = ",type([1, 2, 3]))   # List
print("type({'name':'Asabeneh'}) = ",type({'name':'Asabeneh'})) # Dictionary
print("type({9.8, 3.14, 2.7}) = ", type({9.8, 3.14, 2.7}))    # Set
print("type((9.8, 3.14, 2.7)) = ", type((9.8, 3.14, 2.7)))    # Tuple

print(python_version())
