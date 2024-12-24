from typing import List
class Solution:
    def dfs(self,  grid: List[List[int]], row: int, col: int) -> None:
        
        if grid[row][col]==0:
            return
        # Change the value to zero
        grid[row][col] = 0
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if r>=0 and c>=0 and r<=len(grid)-1 and c<=len(grid[0])-1 and grid[r][c]==1:
                    self.dfs(grid, r, c)


    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Using dfs we can solve this problem

        call dfs only for boundaries, make all the accessible 1 to 0s
        finally count 1's - this approach is entitled to use extra space as program stack
        """
        
        rows = len(grid)
        cols = len(grid[0])
        if rows==1 or cols==1:
            return 0

        # call dfs for first and last column
        for r in range(rows):
            self.dfs(grid, r, 0)
            self.dfs(grid, r, cols-1)
        
        for c in range(1, cols-1):
            self.dfs(grid, 0, c)
            self.dfs(grid, rows-1, c)
        
        
        enclaves = 0
        for row in grid:
            # print(row)
            enclaves += sum(row)
        
        return enclaves