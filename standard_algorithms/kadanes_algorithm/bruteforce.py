# https://leetcode.com/problems/maximum-subarray/description/
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        First solution is bruteforce
        Calculate sum of every subarray, record the larges
        """
        largest_sum = float('-inf')
        csum = 0
        for start in range(len(nums)):
            csum = 0
            for end in range(start, len(nums)):
                csum += nums[end]
                largest_sum = max(largest_sum, csum)
            # end for
        # end for
        return largest_sum

        