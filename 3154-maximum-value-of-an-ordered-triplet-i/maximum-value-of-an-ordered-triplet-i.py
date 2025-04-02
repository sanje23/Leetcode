class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ma=float('-inf')
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    ma=max(ma,(nums[i]-nums[j])*nums[k])
        if ma<0:
            return 0
        return ma