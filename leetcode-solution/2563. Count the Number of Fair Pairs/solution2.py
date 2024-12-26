#
from bisect import bisect_left, bisect_right 
from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Sort the nums array
        now for every number in nums, find upper and lower limit.
        keep counting the difference
        """
        
        nums.sort()
        fair_pairs = 0
        for i in range(len(nums)-1):
                        
            # consider on number is nums[i] so remaining scope is from [lower-nums[i], upper-nums[i]]
            # find index of the second number
            li = bisect_left(nums, lower-nums[i], i+1) # li is just larger or equal to than lower-nums[i]
            ui = bisect_right(nums, upper-nums[i], i+1) # ui is just larger to uppwer-nums[i]
            fair_pairs += ui - li
        return fair_pairs

        