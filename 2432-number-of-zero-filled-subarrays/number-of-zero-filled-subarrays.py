class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        curr=0
        for i in range(len(nums)):
            if nums[i]==0:
                curr+=1
                res+=curr
            else:
                curr=0
        return res