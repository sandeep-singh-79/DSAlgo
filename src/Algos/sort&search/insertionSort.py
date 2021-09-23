""" Insertion sort algo
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
        In other words move unsorted element to the left by 1
    break loop and insert X here
end insertionSort

psuedocode:
insertionSort(array)
    for each step from 1 till (array size - 1) (0 index arrays)
        key = item at step
        for each element from (step - 1) till 0 and key is less than current element
            # move current element right by 1
            array[j+1] = array[j]
        array[j + 1] = key
"""

def insertionSort(array, size):
    if size < 2: return array
    if array is None: return []

    for step in range(1, size):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data, 5)
print('Sorted Array in Ascending Order:')
print(data)