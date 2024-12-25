# https://leetcode.com/problems/subarray-sum-equals-k/
import bisect
from typing import List
class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        # Bruteforce
        count = 0
        # All subarrays
        for length in range(1, len(nums)+1): # length of the subarray goes from 1 to n
            for start in range(len(nums)-length+1): # 0 to n-1
                sbarray = nums[start: start+length]
                # print(sbarray)
                if sum(sbarray)==k:
                    count += 1
                # end if 
            # end for
        # end for

        return count


        