class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [None] * n
        suffix = [None] * n
        prefix[0] = nums[0]
        suffix[n-1] = nums[n-1]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[n - i - 1] = suffix[n - i] * nums[n - i - 1]
        
        result = [None] * n
        result[0] = suffix[1]
        result[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            result[i] = prefix[i-1] * suffix[i + 1]
        return result
        