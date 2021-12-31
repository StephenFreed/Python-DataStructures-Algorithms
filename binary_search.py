def binary_search(list,target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return f'{list[midpoint]} is at index {midpoint}'
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return 'Not in list.'


list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13]

answer = binary_search(list_,3)
print(answer)