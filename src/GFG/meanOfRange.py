class Solution:  
    def findMean(self, arr, queries, n, q):
        meanArr = list()
        for i in range(0, len(queries), 2):
            left = queries[i]
            right = queries[i+1]
            
            sum = 0
            counter = right - left + 1
            for j in range(left, right+1):
                sum += arr[j]
            
            meanArr.append(sum//counter)
        return meanArr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n,q = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    queries = list(map(int,input().strip().split()))
    ob=Solution()
    v = ob.findMean(arr, queries, n, 2*q)
    print(*v)
    
# } Driver Code Ends