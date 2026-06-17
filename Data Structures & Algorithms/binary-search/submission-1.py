class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1, p2 = 0, len(nums) - 1

        while p1 <= p2:
            pm = (p1 + p2) // 2
            if nums[pm] == target:
                return pm
            elif nums[pm] < target:
                p1 = pm + 1   # target is in the right half
            else:
                p2 = pm - 1   # target is in the left half

        return -1
