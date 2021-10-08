# Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and  arr[i]+arr[j] is divisible by k.

# Example
# arr = [1, 2, 3, 4, 5, 6]
# k = 5
# Three pairs meet the criteria: [1, 4], [2,3] and [4, 6].

# Function Description
# Complete the divisibleSumPairs function in the editor below.
# divisibleSumPairs has the following parameter(s):
# int n: the length of array 
# int ar[n]: an array of integers
# int k: the integer divisor
# Returns
# - int: the number of pairs

# Input Format
# The first line contains 2 space-separated integers, n and k.
# The second line contains n space-separated integers, each a value of arr[i].

# Constraints
# - 2 <= n <= 100
# - 1 <= k <= 100
# - 1 <= arr[i] <= 100

# Sample Input
# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

# Sample Output
#  5

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n: int, k: int, ar: list) -> int:
    if n > 1 and k > 0:
        countPairs:int = 0
        pairs: dict = {}

        for i in range(n):
            for j in range(i+1, n):
                if(ar[i], ar[j]) in pairs.keys():
                    countPairs += 1
                    continue
                else:
                    if ((ar[i] + ar[j]) % k == 0):
                        countPairs += 1
                        pairs[(ar[i], ar[j])] = ((ar[i] + ar[j]) % k)
    
    return countPairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
