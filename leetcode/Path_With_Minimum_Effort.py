class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        res = 0
        heap = [(0, 0, 0)]
        while heap:
            diff, x, y = heappop(heap)
            res = max(res, diff)
            
            if x == m-1 and y == n-1:
                return res
            
            if heights[x][y] == 0:
                continue