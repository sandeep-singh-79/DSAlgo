""" 
Iterative Method:
do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > arr[mid]) // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1

Recursive Method:
binarySearch(arr, x, low, high)
    if low > high
        return False 
    else
        mid = (low + high) / 2 
        if x == arr[mid]
            return mid
        else if x > arr[mid]        // x is on the right side
            return binarySearch(arr, x, mid + 1, high)
        else                               // x is on the right side
            return binarySearch(arr, x, low, mid - 1)
"""

def binarySearchIterative(arr: list, toSearch: int) -> int:
    if arr is None or len(arr) == 0: return -1
    
    (low, high) = (0, len(arr))
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == toSearch: return mid
        elif toSearch < arr[mid]: high = mid-1
        elif toSearch > arr[mid]: low = mid+1
    
    return -1

def binarySearchRecursive(arr:list, toSearch:int, left:int, right:int) -> int:
    if arr is None or len(arr) == 0: return -1

    mid = left + (right - left)//2
    if arr[mid] == toSearch:
        return mid
    elif toSearch < arr[mid]:
        return binarySearchRecursive(arr, toSearch, left, mid-1)
    else: # if (toSearch > arr[mid])
        return binarySearchRecursive(arr, toSearch, mid+1, right)



array = [3, 4, 5, 6, 7, 8, 9]
x = 4

resultIter = binarySearchIterative(array, x)
resultRecursion = binarySearchRecursive(array, x, 0, len(array))

if resultIter != -1:
    print("Element is present at index " + str(resultIter))
else:
    print("Not found")
if resultRecursion != -1:
    print("Element is present at index " + str(resultRecursion))
else:
    print("Not found")
