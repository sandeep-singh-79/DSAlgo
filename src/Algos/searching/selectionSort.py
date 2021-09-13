""" Selection Sort Algo
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
"""

def selectionSort(array, n):
    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)