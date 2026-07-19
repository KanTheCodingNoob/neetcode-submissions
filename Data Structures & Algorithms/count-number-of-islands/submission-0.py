class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        visited = "-1"

        def search(i, j):
            if grid[i][j] == visited or grid[i][j] == "0":
                return
            # Boolean Flag
            grid[i][j] = visited

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
                if grid[i][j] == "1":
                    count += 1
                    search(i, j)
        
        return count