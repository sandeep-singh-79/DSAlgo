# find out the number of rotations of a sorted array. Such an array is also called a circularly sorted array
# The assumptions are: Firstly, the array is sorted. Secondly, there is no duplication of elements
# The naive approach would be to find out the index of the min element. The index will signify the number of
# rotations to the right.

""" 
naive approach pseudocode: O(n)
min <-- A[0]
minIdx = 0

loop over the array
    if min > A[i]
        replace min with A[i]
        minIdx = i
"""

def countRotationsOfCircularlySortedArray(arr: list, low: int, high: int) -> int:
    if arr[low] < arr[high]: return low
    
    # the smallest element in a circularly rotated array will have the property
    # where it will be less than its immediate neighbours
    (n, mid) = ((high - low), (low+high)//2)
    (next, prev) = ((mid + 1)%n, (mid + n -1)%n)
    if (arr[mid] <= arr[next]) and (arr[mid]<=arr[prev]): return mid

    # if neither of the above two are applicable then we start reducing the search space
    elif arr[mid] <= arr[high]: return countRotationsOfCircularlySortedArray(arr, low, mid - 1)
    elif arr[mid] >= arr[low]: return countRotationsOfCircularlySortedArray(arr, mid + 1, high) 


arr = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]

rotationCount = countRotationsOfCircularlySortedArray(arr, 0, (len(arr)-1))
print(f"The array has been rotated {rotationCount} times.")