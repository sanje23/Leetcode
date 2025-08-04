class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        t=sorted(nums1+nums2)
        n=len(t)
        if n%2!=0:
            return t[n//2]
        return (t[n//2]+t[n//2-1])/2
        