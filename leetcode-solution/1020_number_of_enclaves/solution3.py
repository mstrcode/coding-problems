from collections import deque
from typing import List
class Solution:
    def bfs(self,  grid: List[List[int]], row: int, col: int) -> None:
        if grid[row][col]==0:
            return
        grid[row][col]=0
        queue = deque()

        queue.append((row, col))

        while queue:
            r, c = queue.popleft()
            
            neighbours = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for i, j in neighbours:
                if i>=0 and j>=0 and i<len(grid) and j<len(grid[0]) and grid[i][j]==1:
                    grid[i][j] = 0
                    queue.append((i,j))    
        


    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        BFS:
        Only run bfs for boundaries, make all the accessible 1 to 0
        finally count total 1's
        """
        
        rows = len(grid)
        cols = len(grid[0])
        if rows==1 or cols==1:
            return 0

        # call dfs for first and last column
        for r in range(rows):
            self.bfs(grid, r, 0)
            self.bfs(grid, r, cols-1)
        
        for c in range(1, cols-1):
            self.bfs(grid, 0, c)
            self.bfs(grid, rows-1, c)
        
        
        enclaves = 0
        for row in grid:
            # print(row)
            enclaves += sum(row)
        
        return enclaves