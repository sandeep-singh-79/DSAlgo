#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    if n > 2:
        sockPairs = 0

        sockPairSet = set(ar)
        sockPairCount = [ar.count(sock) for sock in sockPairSet]
        
        for sockPair in sockPairCount:
            if sockPair > 2: sockPairs += sockPair//2
    
    return sockPairs

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
