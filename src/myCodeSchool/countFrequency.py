#  find out number of occurrences of a number in a sorted array using binary search in O(log n) time
#  naive solution consists of iterating over the array and count the required element
#  naive solution can be further improved by exiting the loop when the element greater than the
#  searched for element is found. However, this will also have the worse-case complexity of O(n)

def findCountOfNumber(arr, x) -> int:
    if arr is None or len(arr) == 0: return -1

    (lastOccurance, firstOccurance) = (findOccurance(arr, x, False), findOccurance(arr, x, True))
    if firstOccurance == -1: return -1
    return lastOccurance - firstOccurance + 1


def findOccurance(arr, x, firstOccuranceFlag: bool) -> int:
    low, high = 0, len(arr)-1
    result = -1

    while low <= high:
        mid = (low+high)//2
        if x == arr[mid]:
            result = mid
            if firstOccuranceFlag: high = mid - 1
            else: low = mid + 1
        elif x < arr[mid]: high = mid - 1
        else: low = mid+1
    return result


array = [1, 1, 3, 3, 5, 5, 5, 5, 5, 9, 9, 11]
x = 5

count = findCountOfNumber(arr=array, x=x)

if count != -1:
    print("Number %d occurs %d times in the array"  % (x, count))
else:
    print("Not found")
