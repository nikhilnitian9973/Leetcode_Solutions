class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        if not grid[0]:
            return grid
        for i in range(k):
            for row in grid:
                a = row.pop()
                row.insert(0,a)
            
            for i in range(len(grid)-1,0,-1):
                grid[i][0],grid[i-1][0] = grid[i-1][0],grid[i][0]
        return grid
            
