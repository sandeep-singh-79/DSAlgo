# Given an array A of positive integers. Your task is to find the leaderLst in the array.
# An element of array is leader if it is greater than or equal to all the elements to its right side.
# The rightmost element is always a leader. 

 

# Example 1:

# Input:
# n = 6
# A[] = {16,17,4,3,5,2}
# Output: 17 5 2
# Explanation: The first leader is 17 
# as it is greater than all the elements
# to its right.  Similarly, the next 
# leader is 5. The right most element 
# is always a leader so it is also 
# included.
 

# Example 2:

# Input:
# n = 5
# A[] = {1,2,3,4,0}
# Output: 4 0

class Solution:
    def leaders(self, A, N):
        if N == 1: return A
        if A is None: return []
        if len(A) < N or len(A) > N: raise ValueError("Length of supplied array is less than or greater than the supplied N")

        leaderLst = []
        j = 0

        for i in range(N):
            if i:
                if i == N-1:
                    leaderLst.append(A[i])
                if A[i] > A[i - 1] and A[i] > A[i+1]:
                    leaderLst.append(A[i])
                    j += 1
            else:
                if A[i] > A[i + 1]:
                    leaderLst.append(A[i])
                    j += 1
        
        return leaderLst
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaderLst(A,N)
        
        for i in A:
            print(i)
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends