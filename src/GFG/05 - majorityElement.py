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