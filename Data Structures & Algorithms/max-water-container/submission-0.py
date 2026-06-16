class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVal = 0
        p1, p2 = 0, len(heights) - 1
        while p1 < p2:
            dis = p2 - p1
            volume = dis * min(heights[p1], heights[p2])
            if volume > maxVal:
                maxVal = volume
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxVal