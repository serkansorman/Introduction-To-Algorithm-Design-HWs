def hasMatchingIndex(arr):
    return binarySearch(arr, 0, len(arr) - 1)

#Checks whether the A[i] = i using Binary Search
def binarySearch(arr, low, high): 
    if high >= low:
        
        mid = (low + high)//2
        if mid == arr[mid]:    
            return True 
        if mid > arr[mid]: 
            return binarySearch(arr, (mid + 1), high) 
        else: 
            return binarySearch(arr, low, (mid -1)) 
  
    return False
  
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100] # A[3] == 3
print(hasMatchingIndex(arr))