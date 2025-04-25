from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        b=len(nums)//2
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
            if freq[i]>b:
                return i