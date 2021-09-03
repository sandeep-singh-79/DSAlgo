""" Given a sorted array A[] of size N, delete all the duplicates elements from A[].
Note: Don't use set or HashMap to solve the problem.


Example 1:

Input:
N = 5
Array = {2, 2, 2, 2, 2}
Output: 2
Explanation: After removing all the duplicates 
only one instance of 2 will remain.
Example 2:

Input:
N = 3
Array = {1, 2, 2}
Output: 1 2 

Your Task:  
You don't need to read input or print anything. Complete the function remove_duplicate() which takes the array A[] and its size N as input parameters and modifies it in place to delete all the duplicates. The function must return an integer X denoting the new modified size of the array. 
Note: The generated output will print all the elements of the modified array from index 0 to X-1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1) """

class Solution: 
    def remove_duplicate(self, A, N):
        if N==0 or A is None: return 0
        if N == 1: return N
        i = 0
        while i < N:
            if i == N-1:break
            if A[i] == A[i+1]:
                del A[i]
                N = len(A)
            else: i +=1
        
        return len(A)

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends