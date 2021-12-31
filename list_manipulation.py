my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [1, 2, 3]

for element in my_list_1[:]:
    if element in my_list_2:
        my_list_1.remove(element)

print(my_list_1)


