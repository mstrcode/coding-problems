from bisect import bisect_left
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        nums.sort()
        for i in range(len(nums)):
            f = nums[i]
            s = nums[i]+k
            si = bisect_left(nums, s, i+1)
            if si < len(nums) and nums[si]==s:
                pairs.add((f,s))
        return len(pairs)
        