# Still bruteforce but O(n^2)
from typing import List

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        # This time, start thinking
        for start in range(len(nums)):
            csum = 0
            for end in range(start, len(nums)):
                csum += nums[end]
                if csum==k:
                    count += 1
                # end if
            # end for 
        # end for
        return count

