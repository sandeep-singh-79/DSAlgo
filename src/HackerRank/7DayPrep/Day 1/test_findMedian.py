#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    if arr is None or len(arr) == 0: return
    if len(arr) == 1: return arr[0]

    arr.sort()
    length = len(arr)
    
    median = 0
    if length % 2 == 0:
        mid = length//2
        median = (arr[mid] + arr[mid+1])//2
    else:
        median = length//2
    
    return arr[median]

