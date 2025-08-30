class Solution:
    def reverseBits(self, n: int) -> int:
        t=str(bin(n)[2:])
        q=t[::-1]+'0'*(32-len(t))
        return int(q,2)