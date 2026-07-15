class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                hashmap[n] += 1
        for key, val in hashmap.items():
            if val > 1:
                return key
        return -1