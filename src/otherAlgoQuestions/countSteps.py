#!/bin/python3

#
# Complete the 'countMoves' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def allElementsEqual(numbers: list, n: int) -> bool:
    for i in range(1, n):
        if numbers[i] != numbers[0]:
            return False
    
    return True


def countMoves(numbers):
    if numbers == None or len(numbers) == 0: raise ValueError()
    if len(numbers) == 1: return 0
    
    n, i = len(numbers), 1
    steps, allSame = 0, False
    
    allSame = allElementsEqual(numbers, n)
    if allSame == True: return steps
    
    allSame = False
    while allSame != True:
        # find the max element in the list and fix it
        fixedIdxs = [i for i,d in enumerate(numbers) if d == max(numbers)]
        fixedIdx = fixedIdxs[-1]
        # increment the rest of the values
        for idx in range(n):
            if fixedIdx != idx:
                numbers[idx] += 1
        # increment the step counter
        steps += 1
        # check if all the values are same now
        allSame = allElementsEqual(numbers, n)
    
    return steps
    
        
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    print( countMoves(numbers))

    # fptr.write(str(result) + '\n')

    # fptr.close()