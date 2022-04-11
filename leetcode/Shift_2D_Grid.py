class Solution:
   def shiftGrid(self, grid, k) :
       m, n = len(grid), len(grid[0])
       if (k := k%(m*n)) == 0:
           return grid
       count = i = 0
       while count < m*n:
           r, c = divmod(i, n)
           curr, j = grid[r][c], (i+k)%(m*n)  # get initial element and its final position
           while True:
               r, c = divmod(j, n)
               grid[r][c], curr = curr, grid[r][c]  # perform swap operation
               count += 1  # increment swap counter
               if j == i:  # initial index reached
                   break
               j = (j+k)%(m*n)
           i += 1  # increment initial index if not all elements have been swapped
       return grid