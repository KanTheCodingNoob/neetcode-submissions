class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = 0
        
        max_seq = 0
        for key in hashmap:
            if key - 1 not in hashmap:
                array = [key]
                while True:
                    if array[-1] + 1 in hashmap:
                        array.append(array[-1] + 1)
                    else:
                        break
                size = len(array)
                if size > max_seq:
                    max_seq = size
        return max_seq