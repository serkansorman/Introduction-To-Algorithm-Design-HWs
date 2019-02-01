#Calculate left half array contiguous subset with the largest sum
def leftOppositeSum(arr, start, mid, end):
    tempSum = 0 
    left_sum = float('-inf')

    for i in range(mid,start+1,-1):
        tempSum += arr[i]
        left_sum = max(tempSum, left_sum)       
    return left_sum;

#Calculate right half array contiguous subset with the largest sum
def rightOppositeSum(arr, start, mid, end):
    tempSum = 0 
    right_sum = float('-inf')

    for i in range(mid + 1, end + 1):
        tempSum += arr[i]  
        right_sum = max(tempSum, right_sum)       
    return right_sum;
  

def largestSum(arr, start, end) : 
      
    if (start == end): 
        return arr[start] 

    mid = (start + end) // 2 
    return max(largestSum(arr, start, mid), 
               largestSum(arr, mid+1, end), 
               (leftOppositeSum(arr, start, mid, end) + rightOppositeSum(arr, start, mid, end))) 
         
arr = [5, -6, 6, 7, -6, 7, -4, 3]
print( largestSum(arr, 0, len(arr)-1)) 