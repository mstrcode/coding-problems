from bisect import bisect_left, bisect_right
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs = set()
        count = 0
        nums.sort()
        i=0
        while i<len(nums):
            f = nums[i]
            s = nums[i]+k
            si = bisect_left(nums, s, i+1)
            if si < len(nums) and nums[si]==s:
                # pairs.add((f,s))
                count += 1
            i += 1
            while i<len(nums) and nums[i]==nums[i-1]:
                i += 1
        return count
        