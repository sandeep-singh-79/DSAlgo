""" Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N 
is an element that appears more than N/2 times in the array.
 

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
"""

class Solution:
    def majorityElement(self, A, N):
        """
        A majority element is one that appears more than N/2 times in the given array
        """
        majorityCount = N//2

        items = self.countItems(A)

        majorityItems = list()
        for key in items.keys():
            if items[key] > majorityCount:
                return key
        
        return -1

    def countItems(self, arr):
        items = dict()
        for item in arr:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        return items

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends