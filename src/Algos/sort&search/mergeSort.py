""" 
MergeSort(A, p, r):
    if p > r 
        return
    q = (p+r)/2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)

merge(A, p, q, r):
    Have we reached the end of any of the arrays?
    No:
        Compare current elements of both arrays 
        Copy smaller element into sorted array
        Move pointer of element containing smaller element
    Yes:
        Copy all remaining elements of non-empty array
"""
""" 
pseudocode
mergeSort(A):
    if len(A) == 1 return A

    median == len(A)//2
    leftArr = A[:median]
    rightArr = A[median+1:]
    
    mergeSort(leftArr)
    mergeSort(rightArr)

    merge(A, leftArr, rightArr)

merge(A, L, R):
    i = j = k = 0

    while i < len(L) && j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        A[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        A[k] = L[i]
        k += 1
        j += 1

"""

def mergeSort(A):
    print(f"A: {A}")
    if len(A) == 1: return A

    median = len(A)//2
    leftArr = A[:median]
    rightArr = A[median:]
    
    mergeSort(leftArr)
    mergeSort(rightArr)

    merge(A, leftArr, rightArr)
    print(f"post merge A: {A}")

def merge(A, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    print(f"In merge - after first while loop A is: {A}")
    print(f"i: {i}; j: {j}; k: {k}; len(L): {len(L)}; len(R): {len(R)}")
    while i < len(L):
        A[k] = L[i]
        k += 1
        i += 1
    print(f"A: {A}")
    
    while j < len(R):
        A[k] = R[j]
        k += 1
        j += 1
    print(f"A: {A}")


# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print(f"Sorted array is: {array}")