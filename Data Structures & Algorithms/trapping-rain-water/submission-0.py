class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        area = 0
        prefix = [None] * n
        suffix = [None] * n
        prefixMax = suffixMax = 0

        for i in range(n):
            if height[i] > prefixMax:
                prefixMax = height[i]
            prefix[i] = prefixMax
            if height[n - 1 - i] > suffixMax:
                suffixMax = height[n - 1 - i]
            suffix[n - 1 - i] = suffixMax
        
        for i in range(n):
            area += min(prefix[i], suffix[i]) - height[i]
        
        return area
