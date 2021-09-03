# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

# Example 1:

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# iterate through arr and populate newArr with the diff of k and arr[i]
# iterate through newArr till i-1. check if newArr[i] ==
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6.

# Example 2:

# Input:
# N = 4, X = 2
# arr[] = {1, 1, 1, 1}
# i = 0 =>is arr[i] in new array. No, do not increment counter; newarray[i] = k-arr[i]
# i = 1 =>is arr[i] in new array. Yes, counter++; newarray[i] = k-arr[i]
# i = 2 =>is arr[i] in new array. Yes, counter++; newarray[i] = k-arr[i]
# i = 3 =>is arr[i] in new array. Yes, counter++; newarray[i] = k-arr[i]
# i = 4 =>quit; return counter = 3
# Output: 6
# Explanation: 
# Each 1 will produce sum 2 with any 1.

# Your Task:
# You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

class Solution:
    def getPairsCountNestedLoops(self, arr, n, k):
        if n == 0 or arr is None: return -1

        countOfPairs = 0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] + arr[j] == k: countOfPairs += 1
        
        return countOfPairs
    
    def getPairsCount(self, arr, n, k):
        if n == 0 or arr is None: return -1

        itemFreq = dict()
        for item in arr:
            if item in itemFreq.keys():
                itemFreq[item] = itemFreq[item] + 1
            else:
                itemFreq[item] = 1
        
        pairCount = 0
        for i in range(n):
            diff = k - arr[i]
            if diff in itemFreq.keys():
                pairCount += itemFreq[diff]
            if diff == arr[i]: pairCount -= 1
        
        return pairCount//2


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends