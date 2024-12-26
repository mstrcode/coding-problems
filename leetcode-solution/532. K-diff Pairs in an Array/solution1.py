# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Bruteforce
        pairs = set() # to keep the unique pairs
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i]-nums[j])==k:
                    pairs.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
        return len(pairs)
        