""" Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times.
Find these repeating numbers in O(n) and using only constant memory space.

Example: 

Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
Output: 1, 3, 6

Explanation: The numbers 1 , 3 and 6 appears more
than once in the array.

Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
Output: 3

Explanation: The number 3 appears more than once
in the array.
"""

class Solution:
    def duplicates(self, arr: list, n: int) -> list: 
        if len(arr) == 0 or arr is None: return
        
        frequency = dict()
        
        for i in range(0, n):
            if arr[i] not in frequency:
                frequency[arr[i]] = 1
            else:
                frequency[arr[i]] = frequency[arr[i]] + 1
            
        retVals = list()

        for key in frequency.keys():
            if frequency[key] > 1: retVals.append(key)

        retVals.sort()
        
        if len(retVals) >= 1: return retVals
        else: return [-1]

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        # n = int(input())
        # arr = list(map(int, input().strip().split()))
        # res = Solution().duplicates(arr, n)
        n = 4
        arr = [2, 3, 1, 2, 3]
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()
