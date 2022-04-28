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
        
            curr_height = heights[x][y]
            heights[x][y] = 0
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy

                print(new_x,new_y)