class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()

        m, n = len(board), len(board[0])

        def findWord(currIdx, wordIdx = 0):
            i, j = currIdx[0], currIdx[1]
            if wordIdx == len(word) - 1 and word[wordIdx] == board[i][j]:
                return True
            if word[wordIdx] != board[i][j]:
                return False
            self.visited.add(currIdx)
            currBool = False
            # Up
            if i > 0 and (i - 1, j) not in self.visited:
                currBool = currBool or findWord((i - 1, j), wordIdx + 1)
            # Down
            if i < len(board) - 1 and (i + 1, j) not in self.visited:
                currBool = currBool or findWord((i + 1, j), wordIdx + 1)
            # Left
            if j > 0 and (i, j - 1) not in self.visited:
                currBool = currBool or findWord((i, j - 1), wordIdx + 1)
            # Right
            if j < len(board[0]) - 1 and (i, j + 1) not in self.visited:
                currBool = currBool or findWord((i, j + 1), wordIdx + 1)
            self.visited.remove(currIdx)
            return currBool

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if findWord((i, j)):
                        return True
                    self.visited = set()
        
        return False