class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal = max(piles)
        p1 = 1       
        p2 = maxVal
        minVal = maxVal
        while p1 <= p2:
            pm = (p1 + p2) // 2
            curH = 0
            for p in piles:
                curH += math.ceil(p / pm)
            if curH <= h:
                p2 = pm - 1
                minVal = pm
            elif curH > h:
                p1 = pm + 1

        return minVal