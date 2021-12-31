def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint],target)

list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13]

answer = recursive_binary_search(list_,3)
print(answer)


print(list_[:4])