class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res,c=0,0
        i=len(s)-1

        while i>=0 and s[i]==' ':
            i-=1

        while i>=0 and s[i]!=' ':
            i-=1
            c+=1
                
        return c
            

