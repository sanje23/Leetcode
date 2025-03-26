class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq={0:0,1:0,2:0}
        for i in nums:
            freq[i]+=1
        q=0
        for i in range(q,freq[0]):
            nums[i]=0
            q+=1
        for i in range(q,freq[1]+q):
            nums[i]=1
            q+=1
        for i in range(q,len(nums)):
            nums[i]=2
