class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_color = [0, 0, 0]
        for i in nums:
            no_color[i] += 1

        idx = 0
        for i in range(len(no_color)):
            count = no_color[i]
            while count > 0:
                nums[idx] = i
                idx += 1
                count -= 1