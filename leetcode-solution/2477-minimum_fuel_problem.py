# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

from collections import defaultdict
from math import ceil
from typing import List
class Solution:
    def dfs(self, graph, curr, parent, people=1):
        for nei in graph[curr]:
            if nei!=parent:
                # do not go back to parent
                people += self.dfs(graph, nei, curr)
        if curr!=0:
            # petrol = number_of_cars * edges
            self.petrol += int(ceil(people / self.seats))
        return people


    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        # build the graph
        for x,y in roads:
            adj[x].append(y)
            adj[y].append(x)
        
        self.petrol = 0
        self.seats = seats
        
        self.dfs(adj, 0, -1)
        return self.petrol