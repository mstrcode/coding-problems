class Solution:
    def fpForLimit(self, arr: List[int], limit: int):
        # arr should sorted list of int
        left = 0; right = len(arr)-1
        fair_pairs = 0
        while left < right:
            if arr[left]+arr[right] <= limit:
                fair_pairs += right - left
                left += 1
            else:
                right -= 1
        return fair_pairs
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        sort the numbs
        we want to find the pairs which sum between [lower, upper]
        lets count for [0, upper] and [0, lower-1], different will be the answer
        this can be achieved using two  pointer method
        """
        nums.sort()
        upper_fp = self.fpForLimit(nums, upper)
        lower_fp = self.fpForLimit(nums, lower-1)
        return upper_fp -lower_fp