class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        p1, p2 = 0, m*n - 1

        while p1 <= p2:
            pm = (p1 + p2) // 2
            pm_m = pm // n
            pm_n = pm % n
            if matrix[pm_m][pm_n] == target:
                return True
            elif matrix[pm_m][pm_n] < target:
                p1 = pm + 1
            else:
                p2 = pm - 1
        return False