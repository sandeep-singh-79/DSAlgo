# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4, 4, 1, 3]
# The maximum height candles are 4 units high. There are 2 of them, so return 2.

# Function Description
# Complete the function birthdayCakeCandles in the editor below.
# birthdayCakeCandles has the following parameter(s):
# int candles[n]: the candle heights
# Returns
# int: the number of candles that are tallest

# Input Format
# The first line contains a single integer, m, the size of candles.
# The second line contains n space-separated integers, where each integer i describes the height of candles[i].

# Constraints
# 1. 1 <= n <= 10^5
# 2. 1 <= candles[i] <= 10^7

# Sample Input 0
# 4
# 3 2 1 3
# Sample Output 0
# 2
# Explanation 0
# Candle heights are [3,2,1,3]. The tallest candles are 3 units, and there are 2 of them.

import math
import os
import random
import re
import sys



def birthdayCakeCandles(candles):
    if candles == None or len(candles) == 0: return
    if len(candles) == 1: return [0]
    if len(candles) > 1:
        counts = [0] * (max(candles)+1)
        for i in range(len(candles)):
            counts[candles[i]] += 1
    
    return max(counts)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()