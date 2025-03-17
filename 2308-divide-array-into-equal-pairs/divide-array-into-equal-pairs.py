from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq=defaultdict(int)
        for i in nums:
            freq[i]+=1
        for i,j in freq.items():
            if j%2!=0:
                return False
        return True