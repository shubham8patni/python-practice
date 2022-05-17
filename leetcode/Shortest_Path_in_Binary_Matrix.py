class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs layer by layer
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        n = len(grid)
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0: return -1 # no such path
        grid[0][0] = 1
        frontier = [(0, 0)] # start from top-left
        count = 1 # at least 1 length
        if n == 1: return count # edge case
        while frontier:
            adjs = [] # all adjacent cells
            count += 1
            for x, y in frontier:
                adj = [] # adjacent cells of current cell
                for ix, iy in moves:
                    i = x + ix
                    j = y + iy
                    if 0 <= j < n and 0 <= i < n and grid[i][j] == 0:
                        if i == j == n - 1: return count# reach the destination
                        grid[i][j] = 1 # visited
                        adj.append((i, j))
                adjs.extend(adj)
            frontier = adjs # switch to next layer
        return -1