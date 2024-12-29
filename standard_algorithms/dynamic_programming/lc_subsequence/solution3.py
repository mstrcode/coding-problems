# https://leetcode.com/problems/uncrossed-lines/
# Another wording for longest common subsequence
"""
SOLUTION: Iterative DP
Space complexxity: O(n)
Time complexity: O(n^2)
"""
from typing import List
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # This problem is another wording for longest common subsequence

        n1 = len(nums1)
        n2 = len(nums2)

        upto_prev = [0]*(n2+1)
        
        for i in range(1, n1+1):
            current = [0]*(n2+1)
            for j in range(1, n2+1):
                if nums1[i-1]==nums2[j-1]:
                    # Match case
                    current[j] = 1 + upto_prev[j-1]
                else:
                    # Non match case
                    current[j] = max(upto_prev[j], current[j-1])
            upto_prev = current
        return upto_prev[-1]