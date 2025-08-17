class Solution:
    def twoSum(self, nums: List[int], target:List[int]):
        res=[]
        for i in range(len(nums)):
            t=target-nums[i]
            for j in range(i+1,len(nums)):
                if t==nums[j]:
                    res=[i,j]
        return res
                
        