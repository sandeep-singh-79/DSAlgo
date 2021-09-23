""" Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.
 """

class Solution:
    def sort012(self,arr,n):
        if len(arr) == 0 or arr is None: return [-1]
        if len(arr) == 1: return arr

        items = self.countItems(arr)
        
        retArr = self.addItemsToRetList(arr, items)
        
        return retArr
    
    def countItems(self, arr):
        items = dict()
        for item in arr:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        return items
    
    def addItemsToRetList(self, arr, items):
        keys = [*items]
        keys.sort()
        retArr = list()
        for key in keys:
            retArr.extend([key] * items[key])
        
        return retArr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        arr = ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends