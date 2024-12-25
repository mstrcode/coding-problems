
from collections import Counter
from typing import List
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
        result order will be depending upon queries i.e. we have remember the order of queries.

        we can use sorting of logs and queries and two pointer method
        
        Steps
        sort log and queries on time
        try to remember index of queries because finally answer has to be on original queries order
        have two pointers, lptr, rptr
            lptr will be used to maintain lower limit of the time range
            rptr will be used to maintain upper limit of the time range
        keep counting (+/-) based on what range you're running in.
        save the results in order of original queries provided 
        """
        # sort logs on time of request 
        logs.sort(key=lambda x: x[1]) # TC: O(nlogn)
        lptr = rptr = usdsrvr = 0
        unused_srvr, req_counts = [0]*len(queries), Counter()
        
        # run a loop for sorted queries keeping idx in consideration
        for t, idx in sorted([[t, idx] for idx,t in enumerate(queries)]): # O(nlogn)
            # run right pointer upto upper limit of current query
            # and increased used server numbers
            while rptr < len(logs) and logs[rptr][1] <= t:
                server_id = logs[rptr][0]
                req_counts[server_id] += 1
                # Only counts distinct number of servers in current time range
                usdsrvr += req_counts[server_id]==1
                rptr += 1
            
            while lptr < rptr and logs[lptr][1] < t-x:
                server_id = logs[lptr][0]
                req_counts[server_id] -= 1
                # Only subtracts if zero requests on that server in current time range
                usdsrvr -= req_counts[server_id]==0
                lptr += 1
            
            unused_srvr[idx] = n - usdsrvr
        # end for: [TC: O(n)]
        return unused_srvr