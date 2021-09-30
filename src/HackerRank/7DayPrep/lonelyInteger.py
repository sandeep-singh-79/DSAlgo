# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# a = [1, 2, 3, 4, 3, 2, 1]
# The unique element is 4.

# Function Description
# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
# int a[n]: an array of integers
# Returns
# int: the element that occurs only once
# Input Format

# The first line contains a single integer, n, the number of integers in the array.
# The second line contains  space-separated integers that describe the values in a.

# Constraints
# 1 <= n <= 100
# It is guaranteed that n is an odd number and that there is one unique element.
# 0 <= a[i] <= 100, where 0 <= i <= n.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    if a is None or (len(a) == 0): return
    if len(a) == 1: return a[0]

    maxElement = max(a)
    frequencies = [0] * (maxElement+1)

    for i in range(len(a)):
        frequencies[a[i]] += 1
    
    for i in range(len(frequencies)):
        if frequencies[i] == 1:
            return i;

def lonelyInteger(a):
    if a is None or (len(a) == 0): return
    if len(a) == 1: return a[0]

    frequencies = {}

    for i in range(len(a)):
        key = a[i]
        if key in frequencies.keys(): frequencies[key] += 1
        else: frequencies[key] = 1
    
    # for k in frequencies.keys():
    #     if frequencies[k] == 1: return k
    # filteredDict = {(k,v) for (k, v) in frequencies.items() if v == 1}
    filteredDict = dict((k, v) for k, v in frequencies.items() if v == 1)

    # return (filteredDict.pop()[0])
    return list(filteredDict.keys())[0]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyInteger(a)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
