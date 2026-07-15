class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = set()
        for n in nums:
            if n not in hashmap:
                hashmap.add(n)
            else:
                return n