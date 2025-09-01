class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        s=[]
        for i in nums:
            s.append(int(i))
        s.sort()
        return str(s[len(s)-k])
        