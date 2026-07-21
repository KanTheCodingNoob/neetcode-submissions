class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        array = [0] * n
        array[0] = cost[0]
        array[1] = cost[1]

        for i in range(2, n):
            array[i] = min(array[i - 1], array[i - 2]) + cost[i]

        return min(array[-1], array[-2])
