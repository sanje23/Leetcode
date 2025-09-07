class Solution:
    def sumZero(self, n: int) -> List[int]:
        t=int(n/2)
        res=[]
        for i in range(1,t+1):
            res.append(i)
            res.append(-i)
        if n%2!=0:
            res.append(0)
        return res
