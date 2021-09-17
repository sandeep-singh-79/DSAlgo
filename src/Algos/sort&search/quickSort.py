""" 
quickSort(array, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
    quickSort(array, leftmostIndex, pivotIndex - 1)
    quickSort(array, pivotIndex + 1, rightmostIndex)

partition(array, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
    if element[i] < pivotElement
        swap element[i] and element[storeIndex]
        storeIndex++
  swap pivotElement and element[storeIndex+1]
  return storeIndex + 1
"""

def partitionWithRightMostPivotElement(arr: list, leftIdx: int, rightIdx: int) -> int:
    (pivot, i) = (rightIdx, (leftIdx - 1))
    
    for j in range(leftIdx, rightIdx):
        if arr[j] <= arr[pivot]:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
        
    # last swap is outside the loop
    (arr[i+1], arr[rightIdx]) = (arr[rightIdx], arr[i+1])
    
    return i+1


def partitionWithleftMostPivotElement(arr: list, leftIdx: int, rightIdx: int) -> int:
    if leftIdx < rightIdx:
        pivot = leftIdx
        (i, j) = (leftIdx, rightIdx)

        while i < j:
            while arr[i] <= arr[pivot] and i < rightIdx: i += 1
            while arr[j] > arr[pivot]: j -= 1
            if i < j:
                (arr[i], arr[j]) = (arr[j], arr[i])
        
        (arr[pivot], arr[j]) = (arr[j], arr[pivot])
    
    return j


def partitionWithMiddlePivotElement(arr, start, end):
    (i, j) = (start, end)
    pivotElement = arr[(start+end)//2]

    while i <= j:
        while arr[i] < pivotElement: i += 1
        while arr[j] > pivotElement: j -= 1
        if i <= j:
            (arr[i], arr[j]) = (arr[j], arr[i])
            i += 1
            j -= 1
    
    return i

def quickSort(arr: list, leftIdx: int, rightIdx: int):
    if leftIdx < rightIdx:
        #pivotIdx = partitionWithRightMostPivotElement(arr, leftIdx, rightIdx)
        pivotIdx = partitionWithleftMostPivotElement(arr, leftIdx, rightIdx)
        quickSort(arr, leftIdx, pivotIdx - 1)
        quickSort(arr, pivotIdx + 1, rightIdx)
        
        #code with middle element as pivot
        # pivotIdx = partitionWithMiddlePivotElement(arr, leftIdx, rightIdx)
        # if leftIdx < pivotIdx-1:
        #     quickSort(arr, leftIdx, pivotIdx-1)
        # if rightIdx > pivotIdx:
        #     quickSort(arr, pivotIdx, rightIdx)


#data = [8, 7, 2, 1, 0, 9, 6]
data = [2, 6, 5, 3, 8, 7, 1, 0]
size = len(data)

print(f"Unsorted Array: {data}")

quickSort(data, 0, size - 1)

print(f"Sorted Array in Ascending Order: {data}")