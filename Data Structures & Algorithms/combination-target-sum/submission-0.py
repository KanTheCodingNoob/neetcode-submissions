class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(idx):
            total = sum(sol)
            if total == target:
                res.append(sol[:])
                return
            elif total > target:
                return

            for i in range(idx, n):
                sol.append(nums[i])
                backtrack(i)
                sol.pop()
        
        backtrack(0)
        return res