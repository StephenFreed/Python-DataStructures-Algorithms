

with open('how_many_lines.txt', 'a') as my_file:
    my_file.write('This is new')


with open('how_many_lines.txt', 'r') as my_file:

    lines_list = my_file.read()
    
print(lines_list)



import csv

test_dict = [[1,2,3],[4,5,6],[7,8,9]]
with open('csv_test.txt', 'w') as myfile:
    csv_writer = csv.writer(myfile)
    for elm in test_dict:
      csv_writer.writerow(elm)


