#  find out number of occurrences of a number in a sorted array using binary search in O(log n) time

def findCountOfNumber(arr, x) -> int:
    if arr is None or len(arr) == 0: return -1

    (lastOccurance, firstOccurance) = (findLastOccurance(arr, x), findFirstOccurance(arr, x))
    if firstOccurance == -1: return -1
    return lastOccurance - firstOccurance + 1


def findFirstOccurance(arr, x) -> int:
    low, high = 0, len(arr)-1
    result = -1

    # first first occurance of the number
    while low <= high:
        mid = (low+high)//2
        if x == arr[mid]:
            result = mid
            high = mid - 1
        elif x < arr[mid]: high = mid - 1
        else: low = mid+1
    return result

def findLastOccurance(arr, x) -> int:
    low, high = 0, len(arr)-1
    result = -1

    # first first occurance of the number
    while low <= high:
        mid = (low+high)//2
        if x == arr[mid]:
            result = mid
            low = mid + 1
        elif x < arr[mid]: high = mid - 1
        else: low = mid+1
    return result

array = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
x = 10

count = findCountOfNumber(arr=array, x=x)

if count != -1:
    print("Element %d occurs %d times in the array"  % (x, count))
else:
    print("Not found")
