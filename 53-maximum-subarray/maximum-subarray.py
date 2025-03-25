class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        curr=0
        for i in nums:
            if curr<0:
                curr=0
            curr+=i
            res=max(curr,res)
        return res