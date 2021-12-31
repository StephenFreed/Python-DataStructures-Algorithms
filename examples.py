# Get a list of integers from the user with list comprehension.
numbers = [int(i) for i in input('Enter numbers:').split()]

# Creates list of even numbers. Int important.
even_numbers = [i for i in numbers if (i % 2) == 0]

# Changes list from integers to string.
even_numbers = [str(i) for i in even_numbers]

# Join won't work unless string type.
print('Even numbers only:', even_numbers)
print(','.join(even_numbers))
