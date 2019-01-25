class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0]) if h else 0
        p = 0
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    p += 4
                    if i > 0 and grid[i-1][j]:
                        p -= 2
                    if j > 0 and grid[i][j-1]:
                        p -= 2
        return p
