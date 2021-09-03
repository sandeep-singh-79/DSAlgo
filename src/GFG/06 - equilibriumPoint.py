class Solution:
    def equilibriumPoint(self,A, N):
        if N == 1: return N
        if A is None: return -1
        
        start = 1

        while start < N-1:
            sumLeft = 0
            sumRight = 0
            for i in range(0, start):
                sumLeft += A[i]
            for j in range(start+1, N):
                sumRight += A[j]
            
            if sumLeft == sumRight:
                return start+1
            else:
                start += 1

        return -1

    def equilibriumPoint2(self, A, N):
        if N == 1: return N
        if A is None: return -1
        if len(A) < N or len(A) > 1: raise ValueError("Length of supplied array is less than or greater than the supplied N")

        sumLeft = []
        sumRight = []

        for i in range(N):
            if i:
                sumLeft.append(sumLeft[i-1] + A[i])
                sumRight.append(sumRight[i-1] + A[N - 1 - i])
            else:
                sumLeft.append(A[i])
                sumRight.append(A[N-i])
        
        for j in range(N):
            if sumLeft[j] == sumRight[N - j]:
                return j
        
        return -1


#{ 
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while(T > 0):
        N = int(input())
        A = [int(x) for x in input().strip().split()]

        ob=Solution()

        print(ob.equilibriumPoint2(A, N))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends