class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        res=0
        while r<len(prices):
            if prices[l]<prices[r]:
                res=max((prices[r]-prices[l]),res)
            else:
                l=r
            r+=1
        return res
