class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count=0
        seen=set()
        for f in fruits:
            flag=False
            for j in range(len(baskets)):
                if j not in seen and f<=baskets[j]:
                    seen.add(j)
                    flag=True
                    break
            if not flag:
                count+=1
        return count