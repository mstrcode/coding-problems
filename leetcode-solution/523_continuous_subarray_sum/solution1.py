# https://leetcode.com/problems/continuous-subarray-sum/description/

from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Bruteforce
        # create every subarray and check madi
        for start in range(len(nums)):
            sbsum = nums[start]
            for l in range(start+1, len(nums)):
                sbsum += nums[l]
                # the length is already at-least two
                # no need to check
                if not sbsum % k:
                    return True
        return False        