class Solution:
    def MissingNumber(self,array,n):
        if n == 0 or array is None: return -1
        if n == 1 or len(array) == 1: return array[0]

        sum = 0
        for item in array:
            sum += item
        
        return (n*(n+1)//2) - sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends