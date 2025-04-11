class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def su(n):
            s=0
            while n>0:
                s+=n%10
                n//=10
            return s
        res=0
        for i in range(low,high+1):
            st=str(i)
            n=len(st)
            if n%2==0 and su(int(st[:n//2]))==su(int(st[n//2:])):
                res+=1
        return res