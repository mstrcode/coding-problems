from typing import List
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len  = 0
        start = 0; end = 0
        curr_xor = 0
        while end<len(nums):
            # if addition and xor of these numbers are equal that means
            # their AND option will be zero
            if curr_xor ^ nums[end] == curr_xor + nums[end]:
                max_len = max(max_len, end - start + 1) # [start, end]
                curr_xor ^= nums[end]
                end += 1
            else:
                max_len = max(max_len, end-start) # [start, end), because nums[end] doesn't fit
                curr_xor ^= nums[start]
                start += 1         
        
        return max_len