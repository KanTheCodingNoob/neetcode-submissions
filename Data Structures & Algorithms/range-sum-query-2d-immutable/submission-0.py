class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # range_row = row2-row1
        # range_col = col2-col1
        result_matrix = [row[col1: (col2 + 1)] for row in self.matrix[row1:(row2+1)]]
        total = 0
        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[0])):
                total += result_matrix[i][j]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)