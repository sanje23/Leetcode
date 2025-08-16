class Solution:
    def maximum69Number (self, num: int) -> int:
        res=""
        c=0
        for i in str(num):
            if i=="6" and c==0:
                res+="9"
                c=1
            else:
                res+=i
        return int(res)
            