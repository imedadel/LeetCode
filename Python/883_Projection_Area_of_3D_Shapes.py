class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = sum(v > 0 for row in grid for v in row)
        area += sum(max(row) for row in grid)
        area += sum(max(column) for column in zip(*grid))
        
        
        
        return area
