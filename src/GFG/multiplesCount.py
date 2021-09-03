def getMaxandMinProduct( A, Q, N, M):
    if len(A) == 0 or len(Q) == 0: raise Exception()
    if A is None or Q is None: raise Exception()
    
    retVals = list()
    for idx in range(0, M):
        counter = 0
        for jidx in range(0, N):
            if Q[idx] % 2 == 0:
                if A[jidx] % 2 == 0: 
                    try:
                        if A[jidx] % Q[idx] == 0: counter += 1
                    except ZeroDivisionError:
                        continue
            else:
                try:
                    if A[jidx] % Q[idx] == 0: counter += 1
                except ZeroDivisionError:
                    continue
        retVals.append(counter)
    
    return retVals
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, m = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        ans = getMaxandMinProduct( arr, brr, n, m)
        for i in ans:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends