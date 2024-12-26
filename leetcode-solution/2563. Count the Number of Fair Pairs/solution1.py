# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # fair_pair = []
        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if lower <= nums[i]+nums[j] <= upper:
                    count += 1
        return count