# this is a line comment

'''
this is a docstring
'''

# strings
string_variable = "string 1"
string_variable_2 = 'string 2'
print(string_variable)
print(string_variable_2)
print(string_variable + " " + string_variable_2)

# numbers
a_integer = 5;
a_float = 4.1;
# 3 is a literal

# calulations
# +,-,*,/,%, **

print(5 ** 2)
print(5 % 10)

# input
user_input = input("Tell me something to say: ")
print(user_input)

# boolean variables
boolean_var = True
boolean_var_2 = False
# boolean expressions
boolean_var_3 = 3 != 3
print(type(boolean_var))
print(boolean_var_3)

# if statement
user_name = "Stephen"
if user_name == "Stephen":
    print("statement was true")

# boolean operators
if user_name == "Stephen" and 3 == 3:
    print("true")

if user_name == "Stephen" or 3 == 4:
    print("true")

not_boolean = not 1 + 1 == 2 
print(not_boolean)

# if else statement
age = 19
if age < 18:
    print("Not an adult")
else:
    print("This is an adult")

# if, else if, else:
number = 2
if number == 1:
    print("number is 1")
elif number == 2:
    print("number is 2")
elif number == 3:
    print("number is 3")
else:
    print("number over 3")

# list
heights = [5, 6, 7, 8]
print(heights)

heights.append(9)
print(heights)

# concatentate two lists
heights = heights + [10, 11]
print(heights)

# list indexes
print(heights[0])
print(heights[-1])

heights.remove(11)
print(heights)

# 2D list
twoD_list = [["Stephen", 10], ["Bob", 20]]
print(twoD_list[1])
print(twoD_list[1][0])

# list methods

heights.insert(0, 100)
print(heights)
