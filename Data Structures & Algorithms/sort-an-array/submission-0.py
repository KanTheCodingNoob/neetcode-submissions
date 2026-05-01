class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        length = len(nums)
        half_length = length//2
        first_half = self.sortArray(nums[: half_length])
        second_half = self.sortArray(nums[half_length:])
        return self.merge(first_half, second_half)

    def merge(self, arr1, arr2):
        result = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        return result + arr1[i:] + arr2[j:]