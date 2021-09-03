

class Solution:   
    def peakElement(self,arr, n):
        if n == 0 or arr is None: return -1
        if n == 1: return 0

        arrLen = len(arr)
        for i in range(arrLen):
            if arrLen:
                if i == arrLen - 1 and arr[i] > arr[i-1]: return i
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    return i
            else:
                if arr[i] > arr[i+1]: return i
        return -1


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends