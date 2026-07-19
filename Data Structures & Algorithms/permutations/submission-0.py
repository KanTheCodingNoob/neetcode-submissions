class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        def backtrack(visited):
            if len(sol) == n:
                res.append(sol.copy())
                return
            
            for i in range(n):
                if visited[i] == False:
                    visited[i] = True
                    sol.append(nums[i])
                    backtrack(array)
                    sol.pop()
                    visited[i] = False

        array = [False] * n
        backtrack(array)
        return res