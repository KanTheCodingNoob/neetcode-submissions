class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(idx):
            total = sum(sol)
            if total == target:
                res.append(sol[:])
                return
            elif total > target or idx == n:
                return

            sol.append(candidates[idx])
            backtrack(idx + 1)
            sol.pop()

            while (idx + 1) < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1)

        backtrack(0)
        return res
