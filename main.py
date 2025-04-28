# Beneath each comment write the code and print out the result to check it works

'''LISTS'''

# Create a list and assign it to a variable
list = [1, 2, 3, 4, 5]
print(list)

# Find the length of the list
list_lenght = len(list)
print(list_lenght)

# Append an item to the list
list.append(6)
print(list)

# Find the value of an item in the list a specific index
list[3]
print(list[0]) 

# Set the value of an item at a specific index
list[0] = -1
print(list)

# Check whether an item is in the list
print(2 in list)
print(0 in list)

# Sort the list
unsorted_list = [5, 4, 3, 1, 2]
sorted_list = sorted(unsorted_list)
print(sorted_list)

# Iterate over the list using range, printing out each element and the index
for i in range(len(list)):
    print(i, list[i])

# Iterate over the list without using range, printing out each element
for i in list:
    print (i)

'''TUPLES'''

# Create a tuple and assign it to a variable
tuple = (1, 2, 3, "Marina", "ADA", "course")
print(tuple)

# Find the length of the tuple
tuple_lenght = len(tuple)
print(tuple_lenght)

# Find the value of an item in the tuple a specific index
print(tuple[4])

# Check whether an item is in the tuple
print("ADA" in tuple)
print("Adams" in tuple)

# Iterate over the tuple using range, printing out each element and the index
for i in range(len(tuple)):
    print(i, list[i])

# Iterate over the tuple without using range, printing out each element
for i in list:
    print (i)

'''STRINGS'''

# Create a string and assign it to a variable
string = "My name is Marina"
print(string)

#  Find the length of the string
string_lenght = len(string)
print(string_lenght)

# Find the value of an character in the string a specific index
string[6]
print(string[6])

# Check whether an item is in the string
print("M" in string)

# Concatenate (add) two strings together
print(string + ". She studies at ADA.")

# Create an f-string
print(f"Your name: " + string)

# Split a string using .split
string.split()
print(string.split())

# Join a list of strings using .join
string = " ".join(['My', 'name', 'is', 'Marina'])
print(string)

# Iterate over the string using range, printing out each character and the index
for char in range(len(string)):
    print(char, string[char])

# Iterate over the string without using range, printing out each character
for char in string:
    print(char)

'''DICTIONARIES'''

# Create a dictionary and assign it to a variable
dict = {"name": "Marina", "country": "Russia", "age": 40}
print(dict)

# Find the length of the dictionary
dict_lenght = len(dict)
print(dict_lenght)

# Add a new key/value pair
dict["occupation"] = "dev"
print(dict)

# Replace value for a given key
dict["occupation"] = "soft dev"
print(dict)

# Check whether a key is in the dictionary
print(dict.keys())

# Iterate over keys, printing each key
for key in dict:
    print (key)

# Iterate over over key/value pairs using .items(), printing each key and value
for key, value in dict.items():
    print(key, value)

# '''SETS'''

# Create a set and assign it to a variable
set = {1, 2, "ADA"}
print(set)

# Find the length of the set
set_lenght= len(set)
print(set_lenght)

# Add a new element
set.add("bootcamp")
print(set)

# Remove an element
set.remove(1)
set.remove(2)
print(set)

# Check whether a element is in the set
print("bootcamp" in set)

# Iterate over elements, printing each one out
for i in set:
    print(i)

'''NUMBERS'''

# Add / subtract / multiply 2 numbers
a = 5
b = 10
c = a + b
print(c)

# Divide two numbers using normal (float) division
d = a / b
print(d)

# Divide two numbers using integer division
e = b // a
print(e)

# Find the modulo (remainder) of two numbers
modulo = c % b
print(modulo)

# Check whether a number is even/odd
even = b % 2 == 0
odd = a % 2 != 0
print(even)
print(odd)

# Round a float down to an int (!!)
import math

d = 0.5
d = math.floor(d)
print(d)

# '''FUNCTIONS'''

# Write a function that takes no arguments and call it
def fun_no_args():
    return True

print(fun_no_args())

# Write a function that takes one or more arguments and call it
def fun_with_args(num_1, num_2):
    return num_1 + num_2

num_1 = 5
num_2 = 7
print (fun_with_args(num_1, num_2))

# Write a function that returns a value. Call the function and store the return value in a variable
def return_value():
    return "Hello!"

print(return_value())

# '''LOOPS'''

#  Write a while loop (!!)
i = 1
while i > 5:
    i += 1

print(i)

#  Write a for loop that loops a set number of times (e.g. 10 times) (!)
for i in range(10):
    print(i)

# '''CONDITIONALS'''

#  Write an if/elif/else statement
a = 5
b = 10

if a < b:
    print("a is less than b")
elif a == b:
    print("a equals b")
else:
    print("a is more than b")

# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=

if a == b:
    print("a is equal b")
if a != b:
    print("a isn't equal b")
if a < b:
    print("a is less than b") 
if a > b:
    print("a is more than b")
if a <= b:
    print("a is less or equal b")
if a >= b:
    print("a is more or equal b")

# if a == b
if a == b:
    print("a is equal b once again")


# '''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable
list1 = [1, 2, 3]
list2 = [10, 20, 30]
nested_list = [list1, list2]

print(nested_list)

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
print(nested_list[1][2])

# Iterate through the nested data structure using range (!!!)
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(nested_list[i][j])

# Iterate through the nested data structure without using range (!!!)
for list in nested_list:
    for item in list:
        print(item)

# '''REMINDER'''

# You're doing great and you got this!
