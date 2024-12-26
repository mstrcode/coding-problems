# https://leetcode.com/problems/longest-nice-subarray/
from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        Think - every pair in sub array, bitwise AND is equal to 0
        position of one in binary representation of every number, should not repeat
        i.e
        5 has one at 3rd and 1st place i.e. 101, in the same sub array, both the places
        1 should come in any number, that's the reason & of these numbers will be zero 
        """
        max_len = 0
        left = 0
        curr_xor = 0

        for right in range(len(nums)):
            
            # check the current subarray i.e. [left, right] is nice subarray or not
            # curr_xor is xor of all numbers from [left, right)
            # skip all lefts till & of xor and nums[right] is not equal to zero
            # to understand the problem take example of
            # 1 2 4 8 5 2 4
            # curr_xor & nums[right], we are removing nums[left] one by one as soon as left = right - 1 curr_xor itself will become zero so
            # left will never exceed right
            while curr_xor & nums[right] != 0:
                curr_xor ^= nums[left] # remove the effect of nums[left]
                left += 1
            # we consider
            curr_xor ^= nums[right]
            max_len = max(max_len, right-left+1)
        return max_len