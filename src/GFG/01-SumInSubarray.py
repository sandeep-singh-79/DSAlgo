""" Given an unsorted array of nonnegative integers, find a continuous subarray which adds to a given number. 
Examples : 

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Output: Sum found between indexes 1 and 4
Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There is no subarray with 0 sum

"""

class Solution:
    def subArraySum(self,arr, n, s): 
        if n == 0 or arr is None: raise Exception()
        if n == 1 and len(arr) > 1: raise Exception()
        
        start = 0
        end = start
        
        sum = arr[start]

        idx = start+1
        
        while idx < n:
            if sum < s:
                sum += arr[idx]
                if idx == n-1:
                    if sum == s:
                        end = idx
                        break
                    else:
                        start += 1
                        idx = start + 1
                        sum = arr[start]
                        continue
                idx += 1
            elif sum == s:
                end = idx - 1
                break
            elif sum > s:
               start += 1
               sum = arr[start]
               idx = start+1
        
        if end > 1: return [start+1, end+1]
        else: return [-1]

        """ subArr = []
        start = 0
        idx = start + 1
        if arr[start] == 0: subArr.append(arr[start])
        while idx < n:
            if idx == n-1:
                start += 1
                idx = start + 1
                continue
            if arr[idx] + arr[start] == 0:
                subArr.append(arr[start:idx+1])
                start+=1
                idx=start+1
            else:
                idx+=1
        
        subArr.sort()
        print(subArr)
        return len(subArr[len(subArr)-1]) """

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        # T=int(input())
        # while(T>0):
            
            # NS=input().strip().split()
            # N=int(NS[0])
            # S=int(NS[1])
            
            # A=list(map(int,input().split()))
            N, S = 74, 665
            A = [142,112,54,69,148,45,63,158,38,60,124,142,130,179,117,36,191,43,89,107,41,143,65,49,47,6,91,130,171,151,7,102,194,149,30,24,85,155,157,41,167,177,132,109,145,40,27,124,138,139,119,83,130,142,34,116,40,59,105,131,178,107,74,187,22,146,125,73,71,30,178,174,98,113]
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            #T-=1


if __name__ == "__main__":
    main()