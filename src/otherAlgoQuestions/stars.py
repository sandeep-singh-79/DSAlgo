# Input : n= 5
# Output:
# * * * * *
# * * * *
# * * *
# * * 
# *
# * *
# * * *
# * * * *
# * * * * *



def printAstrix(n: int):
    if n > 0:
        i, exitCondition = n, False
        reverseIncrement = False
        
        while exitCondition == False:
            astrix = '*' * i
            print(astrix)
            if reverseIncrement == False:
                i -= 1
                if i == 0:
                    reverseIncrement = True
                    i = 2
            else: 
                i += 1
                if i == n+1:
                    exitCondition = True
        
        # for j in range(i+1, n+1):
        #     astrix = '*' * j
        #     print(astrix)


if __name__ == "__main__":
    printAstrix(5)