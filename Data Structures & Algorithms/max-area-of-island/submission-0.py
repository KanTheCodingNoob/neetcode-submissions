class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxSize = 0
        visited = -1
        self.count = 0

        def search(i, j):
            if grid[i][j] == visited or grid[i][j] == 0:
                return
            # Boolean Flag
            grid[i][j] = visited
            self.count += 1

            atEdgeLeft = j == 0
            atEdgeRight = j == n - 1
            atEdgeTop = i == 0
            atEdgeBottom = i == m - 1

            if not atEdgeLeft:
                search(i, j - 1)
            if not atEdgeRight:
                search(i, j + 1)
            if not atEdgeTop:
                search(i - 1, j)
            if not atEdgeBottom:
                search(i + 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.count = 0
                    search(i, j)
                    maxSize = max(self.count, maxSize)
        
        return maxSize