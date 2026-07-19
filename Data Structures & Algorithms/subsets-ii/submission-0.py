class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        nums.sort()

        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return

            # Do pick sth
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            # Increase the index to not have dupe
            while (i < n - 1) and nums[i] == nums[i + 1]:
                i += 1
            # Don't pick sth
            backtrack(i + 1)
        
        backtrack(0)

        return res