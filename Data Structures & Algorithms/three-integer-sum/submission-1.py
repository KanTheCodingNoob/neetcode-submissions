class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        n = len(sortedNums)
        array = []
        p1, p2, p3 = 0, 1, n - 1
        while p1 < n - 2:
            # Skip duplicates for p1
            if p1 > 0 and sortedNums[p1] == sortedNums[p1 - 1]:
                p1 += 1
                p2 = p1 + 1
                p3 = n - 1
                continue

            while p2 < p3:
                result = sortedNums[p2] + sortedNums[p3]
                if result == -sortedNums[p1]:
                    array.append([sortedNums[p1], sortedNums[p2], sortedNums[p3]])
                    while p2 < p3 and sortedNums[p2] == sortedNums[p2 + 1]:
                        p2 += 1
                    while p2 < p3 and sortedNums[p3] == sortedNums[p3 - 1]:
                        p3 -= 1
                    p2 += 1
                    p3 -= 1
                elif result < -sortedNums[p1]:
                    p2 += 1
                else:
                    p3 -= 1
            p1 += 1
            p2 = p1 + 1
            p3 = n - 1
        return array