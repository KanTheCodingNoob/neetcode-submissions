class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_checks = [set() for _ in range(9)]
        col_checks = [set() for _ in range(9)]
        square_checks = [set() for _ in range(9)]

        # Row Check
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in row_checks[i]:
                    return False
                row_checks[i].add(num)

        # Column Check
        for i in range(9):
            for j in range(9):
                num = board[j][i]
                if num == '.':
                    continue
                if num in col_checks[i]:
                    return False
                col_checks[i].add(num)

        # Square Check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for l in range(i, i + 3):
                    for k in range(j, j + 3):
                        num = board[l][k]
                        if num == '.':
                            continue
                        idx = (i // 3) * 3 + (j // 3)
                        if num in square_checks[idx]:
                            return False
                        square_checks[idx].add(num)
        return True