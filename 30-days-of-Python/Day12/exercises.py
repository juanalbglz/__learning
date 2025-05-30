# Exercises: Day 12
# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
from random import random, randint
import string
def random_user_id(n=6):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}"
    id = ''
    for x in range(n):
        id+= chars[randint(0,91)]
    return(id)
print(random_user_id())
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    n = int(input("How many ids?: "))
    l = int(input("How long?: "))
    for x in range (n):
        print(random_user_id(l))
user_id_gen_by_user()
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    rgb_color = 'rgb'
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rgb = (r,g,b)
    rgb_color+=str(rgb)
    return(rgb_color)
print(rgb_color_gen())

# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    hexchars = '0123456789abcdef'
    hexcolorlst = list()
    for x in range(n):
        color = '#'
        for i in range(6):
            color = color + hexchars[randint(0,15)]
        hexcolorlst.append(color)
    return hexcolorlst
print(list_of_hexa_colors(4))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    rgb_colors = list()
    for x in range(n):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors
print(list_of_rgb_colors(4))
# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(mod, n):
    if mod == 'hexa':
        return(list_of_hexa_colors(n))
    if mod == 'rgb':
        return(list_of_rgb_colors(n))

print(generate_colors('hexa', 3))
print(generate_colors('rgb', 2))
# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    new_lst = []
    while len(lst)>0:
        new_lst.append(lst.pop(randint(0,len(lst)-1)))
    return new_lst
print(shuffle_list([1,2,3,4,5]))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_numbers(n):
    rlist = list()
    while len(rlist)<n:
        new_num = randint(0,9)
        if new_num not in rlist:
            rlist.append(new_num)
    return rlist
print(random_numbers(7))