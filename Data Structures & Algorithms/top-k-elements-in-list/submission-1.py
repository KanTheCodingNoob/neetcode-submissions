class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        reverse_count = [[] for _ in range(len(nums) + 1)]
        for key, val in count_map.items():
            reverse_count[val].append(key)

        result = []
        for i in range(len(reverse_count) - 1, -1, -1):
            for num in reverse_count[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result