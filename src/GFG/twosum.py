""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution:
    def twoSumNaive(self, nums: list, target: int) -> list:
        if nums is None or len(nums) == 0: raise ValueError
        if not nums: return []

        arrLen = len(nums)
        for i in range(arrLen):
            for j in range(i+1, arrLen):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
    
    def twoSum(self, nums: list, target: int) -> list:
        if nums is None or len(nums) == 0: raise ValueError
        if not nums: return []

        sumIdx = {}
        for i in range(len(nums)):
            targetDiff = target - nums[i]
            if targetDiff in sumIdx.keys():
                return [sumIdx[targetDiff], i]
            else:
                sumIdx[nums[i]] = i
        return []


# driver code starts
import math

def main():
        # T=int(input())
        # while(T>0):
            
            # NS=input().strip().split()
            # N=int(NS[0])
            # S=int(NS[1])
            
            # A=list(map(int,input().split()))
            sum = 9
            A = [2, 7 , 11, 15]
            ob=Solution()
            ans=ob.twoSumNaive(A, sum)
            ans2=ob.twoSum(A, sum)
            
            print("Two Sum Naive - O(n squared)")
            print(ans)
                
            print()
            print("Two Sum - O(n)")
            print(ans2)
                
            print()
            
            #T-=1
# driver code ends

if __name__ == "__main__":
    main()