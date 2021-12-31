my_list = ['A','B','C']

# Iterate through the for loop with variable for "index".
index_num = 0
for my_element in my_list:
    print(index_num, my_element)
    index_num += 1

print()
# Use the range function along with len() to get the index number. Use that to print element and index.

for index_num in range(len(my_list)):
    my_element = my_list[index_num]
    print(index_num, my_element)

print()
# enumerate index number and element from list each loop.
for index_num, my_element in enumerate(my_list, start = 1):
    print(index_num, my_element)


# Use index number to print different on last loop.
hourly_temperature = [90, 92, 94, 95]

for index_num, my_element in enumerate(hourly_temperature):
    if  index_num == len(hourly_temperature) - 1:
        print('%d ' % my_element)
    else: 
        print('%d -> ' % my_element, end='')


# Loop that prints different on last loop.
hourly_temperature = [90, 92, 94, 95]

for index_num, my_element in enumerate(hourly_temperature):
    if  index_num == len(hourly_temperature) - 1:
        print('%d ' % my_element)
    else: 
        print('%d -> ' % my_element, end='')



#Print the two-dimensional list.

mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for table_element in mult_table:
    for row_index, row_element in enumerate(table_element):
        if row_index == len(table_element) -1:
            print(row_element)
            
        else:
            print('%d | ' % row_element,end='')
    