# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.
# Your Task:
# You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

# Expected Time Complexity: O(N).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= N <= 105
# -1000 <= A[i] <= 1000, for each valid i

def maxLen(length:int, array:list) -> int:
    """ 
    The method find the largest sub array with sum of 0
    ----------------------------------------------------
    parameters:
    length: length of array
    array: array in which to find the largest subArray
    ----------------------------------------------------
    returns:
    length of the largest sub array
    """
    """ 
    Steps:
    1. map<int, int> pairs; maxSumLength = 0
    2. iterate over the array
    3. Does the sum exist in map
    4. if yes then, update maxSumLength with the diff of current index and index of sum
    5. If no then, add sum with index to map
    6. return maxSumLength
    """
    pairs = dict()
    maxSumLength = 0
    sum = 0

    for i in range(n):
        sum += arr[i]
        if sum == 0:
            maxSumLength = i+1
        else:
            if sum in pairs.keys():
                maxSumLength = i - pairs[sum]
            else:
                pairs[sum] = i
    
    return maxSumLength


if __name__=="__main__":
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(maxLen(length = n, array = arr))