# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in  hour format
# Returns

# string: the time in  hour format
# Input Format

# A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssAM).

# Constraints

# All input times are valid
# Sample Input

# 07:05:45PM
# Sample Output

# 19:05:45

#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    if s is None or len(s) == 0: return
    if not bool(re.match("[0-9]{2}:[0-9]{2}:[0-9]{2}[A|P]M", s)): return

    
    halfOfDay = s[len(s)-2:]
    timeDivisions = s.split(':')
    seconds = timeDivisions[len(timeDivisions) - 1]
    timeDivisions[len(timeDivisions) - 1] = seconds[:2]

    if int(timeDivisions[0]) == 12 and int(timeDivisions[1]) <= 59 and halfOfDay=='AM':
        timeDivisions[0] = '00'
    if halfOfDay == 'PM' and (int(timeDivisions[0]) >= 1 and int(timeDivisions[0]) <= 11) and (int(timeDivisions[1]) >= 0 and int(timeDivisions[1]) <= 59):
        timeDivisions[0] = str(12+int(timeDivisions[0]))
    
    return f"{timeDivisions[0]}:{timeDivisions[1]}:{timeDivisions[2]}"


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
