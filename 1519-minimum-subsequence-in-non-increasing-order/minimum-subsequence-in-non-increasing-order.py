class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        su=sum(nums)
        nums.sort(reverse=True)
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            if curr>su-curr:
                return nums[:i+1]