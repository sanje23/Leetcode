class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        r=[]
        ma,curr=-1,-1
        for i in range(n-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                curr=int(num[i])
            ma=max(ma,curr)
        if ma==-1:
            return ""
        return str(ma)*3

