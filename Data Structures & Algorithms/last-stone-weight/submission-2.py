class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            z = abs(y - x)
            if z != 0:
                heapq.heappush_max(stones, z)
        
        return 0 if (len(stones) == 0) else stones[0]