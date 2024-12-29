from typing import List
class Solution:
    def lcs(self, dp, nums1, nums2, n1, n2):
        if n1==0 or n2==0:
            return 0
        
        if dp[n1][n2] != -1:
            return dp[n1][n2]
        
        if nums1[n1-1]==nums2[n2-1]:
            dp[n1][n2] = 1 + self.lcs(dp, nums1, nums2, n1-1, n2-1)
        else:        
            dp[n1][n2] = max(self.lcs(dp, nums1, nums2, n1-1, n2), self.lcs(dp, nums1, nums2, n1, n2-1))
        return dp[n1][n2]

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # This problem is another wording for longest common subsequence

        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[-1]*(n2+1) for _ in range(n1+1)]
        for i in range(n1):
            dp[i][0] = 0
        
        for j in range(n2):
            dp[0][j] = 0
        
        return self.lcs(dp, nums1, nums2, n1, n2)
