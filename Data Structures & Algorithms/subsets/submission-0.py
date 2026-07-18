class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sols = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sols[:])
                return
            
            # Dont pick nums[i]
            backtrack(i + 1)

            # Do pick nums[i]
            sols.append(nums[i])
            backtrack(i + 1)
            sols.pop()
        
        backtrack(0)
        return res