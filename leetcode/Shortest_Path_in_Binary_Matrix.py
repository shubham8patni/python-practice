class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs layer by layer
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0: return -1 # no such path
        grid[0][0] = 1
        frontier = [(0, 0)] # start from top-left
        count = 1 # at least 1 length
        