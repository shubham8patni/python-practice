class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = -1
        
        obstacleGrid[0][0] = 1
        
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                
                if obstacleGrid[row][col] == -1:
                    continue
                if row > 0:
                    obstacleGrid[row][col] += (obstacleGrid[row-1][col] if obstacleGrid[row-1][col] != -1 else 0)
                if col > 0:
                    obstacleGrid[row][col] += (obstacleGrid[row][col-1] if obstacleGrid[row][col-1] != -1 else 0)
            
        return obstacleGrid[-1][-1]