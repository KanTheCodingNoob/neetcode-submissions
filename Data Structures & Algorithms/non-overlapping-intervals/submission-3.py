class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))
        n = len(intervals)
        count = 0
        end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                count += 1
                end = min(end, intervals[i][1])  # keep the one that ends earlier

        return count
