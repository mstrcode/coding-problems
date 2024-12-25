# https://leetcode.com/problems/count-zero-request-servers/description/
from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Bruteforce
        # Time complexity
        arr = []
        mapping = defaultdict(set)
        for query in queries:
            timeframe = (query-x, query)
            for log in logs:
                if timeframe[0] <= log[1] <= timeframe[1]:
                    mapping[timeframe].add(log[0])
            # end for
        # end for : [TC: O(n^2)]
        
        for query in queries:
            timeframe = (query-x, query)
            arr.append(n-len(mapping[timeframe]))
        # end for: [TC: O(n)]
        return arr