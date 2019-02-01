def merge(left, right):
    
    left_index = 0
    right_index = 0
    result = []
    
    #Check left and right half of list consist of multiple list
    if type(left[0]) is list:
        left = left[0];  #Get one of left lists
    if type(right[0]) is list:
        right = right[0]; #Get one of right lists
        
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(sortedArrays):
   
    if len(sortedArrays) <= 1: 
        return sortedArrays

    # Divide list of lists in half and merge sort recursively
    half = len(sortedArrays) // 2
    left = merge_sort(sortedArrays[:half])
    right = merge_sort(sortedArrays[half:])
    
    return merge(left, right)


print(merge_sort([[1,6,9],
            [8,13,14],
            [0,2,4],
            [10,11,12],
            [3,5,7]]))