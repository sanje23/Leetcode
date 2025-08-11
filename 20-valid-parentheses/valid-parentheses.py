class Solution:
    def isValid(self, s: str) -> bool:
        map={')':'(','}':'{',']':'['}
        st=[]
        for i in s:
            if i in map:
                if st and st[-1]==map[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return not st
        