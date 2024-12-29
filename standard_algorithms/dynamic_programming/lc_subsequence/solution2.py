from typing import List
"""
Space complexity: O(n^2)
Time complexity: O(n^2)

If you observe, for a given i,j, we are only using i-1,j-1, i-1,j, i,j-1 i.e. current row and previous row, current column and previous column
we can still optimize space by using only 2 rows, solution3.py is the optimized version of this solution
"""
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # This problem is another wording for longest common subsequence

        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[-1]*(n2+1) for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = 0
        
        for j in range(n2+1):
            dp[0][j] = 0

        # for row in dp:
        #     print(row)
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1]==nums2[j-1]:
                    # Match case
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # Non match case
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n1][n2]
        