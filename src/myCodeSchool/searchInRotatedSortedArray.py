# perform binary search on a circular sorted array with distinct elements
# naive approach with complexity of O(n) - perform linear search through the array

def findElementInCircularlyRotatedArray(arr: list, low: int, high: int, x: int, recursive: bool) -> int:
    """ 
    The method attempts to find the element in a circularly rotated sorted list.
    It leverages binary search to cut down the complexity to O(log n)

    Parameters:
    -----------------------------------------------------------------------------
    arr: Circularly rotated sorted list. The list should have non-duplicate items
    low: the starting index of the search space
    high: the ending index of the search space
    x  : the item to search for
    recursive: whether to call the recursive solution or the iterative solution

    Return:
    -----------------------------------------------------------------------------
    The method returns the index in case the element is present and -1 if the
    element is not contained in the array 'arr'
    """
    if arr is None or len(arr) == 0: return -1

    if recursive: return __findElementRecursively(arr, low, high, x)
    else: return __findElementIteratively(arr, low, high, x)
    

def __findElementRecursively(arr: list, low, high, x):
    # search for an item using recursive approach
    mid = ((low + high)//2)
    midElement = arr[mid]

    if midElement == x: return mid
    if midElement <= arr[high]:
        if midElement < x and x <= arr[high]:
            return __findElementRecursively(arr, mid+1, high, x)
        else: 
            return __findElementRecursively(arr, low, mid-1, x)
    if midElement >= arr[low]:
        if midElement > x and x >= arr[low]:
            return __findElementRecursively(arr, low, mid-1, x)
        else:
            return __findElementRecursively(arr, mid+1, high, x)
    
    return -1

def __findElementIteratively(arr, low, high, x):
    # search for an item using iterative approach
    while (low <= high):
        mid = ((low + high)//2)
        midElement = arr[mid]
        if midElement == x: return mid
        if midElement <= arr[high]:
            if midElement < x and x <= arr[high]:
                low = mid+1
            else: 
                high = mid-1
        elif midElement >= arr[low]:
            if midElement > x and x >= arr[low]:
                high = mid-1
            else:
                low = mid+1
    
    return -1


arr = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
searchTerm = 25

recursiveItemIdx = findElementInCircularlyRotatedArray(arr, 0, len(arr)-1, searchTerm, True)
iterativeItemIdx = findElementInCircularlyRotatedArray(arr, 0, len(arr)-1, searchTerm, False)

if recursiveItemIdx != -1:
    print(f"The array contains the item {searchTerm} at index {recursiveItemIdx}.")
else:
    print(f"The array does not contain the item {searchTerm}.")
if iterativeItemIdx != -1:
    print(f"The array contains the item {searchTerm} at index {iterativeItemIdx}.")
else:
    print(f"The array does not contain the item {searchTerm}.")
