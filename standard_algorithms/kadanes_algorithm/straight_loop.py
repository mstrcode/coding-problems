from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Second solution:
        If we add nevative numbers, it will keep reducing the sum
        If there is a hope of positive number in future, then only we keep adding the numbers
        but we don't know about the futurte

        so keep adding the number till current sum is >=0 
        """
        largest_sum = -inf
        current_sum = 0

        for n in nums:
            current_sum += n
            largest_sum = max(largest_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return largest_sum

            