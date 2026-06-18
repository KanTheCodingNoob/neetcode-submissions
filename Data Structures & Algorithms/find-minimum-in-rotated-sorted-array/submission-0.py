class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)
        p1, p2 = 0, n - 1
        while p1 <= p2:
            if nums[p1] < nums[p2]:
                res = min(res, nums[p1])
                break
            
            m = (p1 + p2) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[p1]:
                p1 = m + 1
            else:
                p2 = m - 1
        return res

