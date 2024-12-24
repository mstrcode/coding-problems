# https://leetcode.com/problems/number-of-enclaves/description/

from typing import List
class Solution:
    def dfs(self, visited: List[List[bool]], grid: List[List[int]], row: int, col: int) -> int:
        visited[row][col] = True
        if grid[row][col]==0:
            return 0
        if row==0 or col==0 or row==len(grid)-1 or col==len(grid[0])-1:
            self.boundary_accessible = True
        enclaves_visited = 1
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if r>=0 and c>=0 and r<=len(grid)-1 and c<=len(grid[0])-1:
                print(r,c)
                if not visited[r][c]:
                    enclaves_visited += self.dfs(visited, grid, r, c)
        
        return enclaves_visited

    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Using dfs we can solve this problem

        Write a dfs and trace only ones, keep counting how many one's 
        return total number of once if, no any boundary is visited
        """


        visited = [[False]*len(grid[0]) for _ in grid]

        total_enclaves = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j]:
                    self.boundary_accessible = False
                    new_enclaves = self.dfs(visited, grid, i, j)
                    if not self.boundary_accessible:
                        total_enclaves += new_enclaves
        return total_enclaves
        