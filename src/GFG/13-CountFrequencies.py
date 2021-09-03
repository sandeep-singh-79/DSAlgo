""" Given an array A[] of N positive integers which can contain integers from 1 to P where elements can be repeated or can be absent from the array. Your task is to count the frequency of all elements from 1 to N.

Example 1:
Input:
N = 5
arr[] = {2, 3, 2, 3, 5}
P = 5
Output:
0 2 2 0 1
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.

Example 2:
Input:
N = 4
arr[] = {3,3,3,3}
P = 3
Output:
0 0 4 0
Explanation: 
Counting frequencies of each array element
We have:
1 occurring 0 times.
2 occurring 0 times.
3 occurring 4 times.
4 occurring 0 times.

Your Task:
Complete the function frequencycount() that takes the array and n as input parameters and modify the array in place to denote the frequency count of each element from 1 to N. i,e element at index 0 should represent the frequency of 1 and so on.

Note: Can you solve this problem without using extra space (O(1) Space) ! """

class Solution:
    def frequencyCount(self, arr, N, P):
        if arr is None or N == 0: return None

        freq = [0] * P
        for i in range(N):
            freq[arr[i]-1] += 1

        for i in range(P):
            arr[i] = freq[i]
        
        if P < N:
            for i in range(P, N):
                arr[i] = 0
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__=="__main__":
	T=int(input())
	while(T>0):
		N=int(input())
		arr=[int(x) for x in input().strip().split()]
		P=int(input())
		ob=Solution()
		ob.frequencyCount(arr, N, P)
		for i in arr:
			print(i, end=" ")
		print()
		T-=1



# } Driver Code Ends