# Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction. 

# Example 1:

# Input:
# N = 5, D = 2
# arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated
# 0+2 = 3;1+2 = 4; 2+2 = 5;3+2
# by 2 elements, it becomes 3 4 5 1 2.
# Example 2:

# Input:
# N = 10, D = 3
# arr[] = {2,4,6,8,10,12,14,16,18,20}
# Output: 8 10 12 14 16 18 20 2 4 6
# Explanation: 2 4 6 8 10 12 14 16 18 20 
# when rotated by 3 elements, it becomes 
# 8 10 12 14 16 18 20 2 4 6.

class Solution:
    def rotateArrWithSplicing(self,A,D,N):
        if N == 1: return A
        if A is None: return None

        return A[D:] + A[:D]
    
    def rotateArrUsing(self, A, D, N):
        if N == 1: return A
        if A is None: return None

        arr = []
        for i in range(D):
            arr[i] = A[i]
        for j in range(D, N):
            arr[j] = A[j]
        
        return arr
    
    def rotateArr(self, A, D, N):
        if N == 1: return A
        if A is None: return None

        for i in range(D):
            temp = A[0]
            for i in range(N-1):
                A[i] = A[i + 1]
            A[N-1] = temp


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,)
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends