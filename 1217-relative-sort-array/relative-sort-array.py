from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq=defaultdict(int)
        for i in arr1:
            freq[i]+=1
        res=[]
        for i in arr2:
            for j in range(freq[i]):
                res.append(i)
        res2=[]
        for i in arr1:
            if i not in arr2:
                res2.append(i)
        res2.sort()
        res.extend(res2)
        return res