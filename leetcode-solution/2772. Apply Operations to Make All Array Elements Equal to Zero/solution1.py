# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/description/

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        if k==1:
            return True
        
        # lets keep making 0 from left to right
        i=0
        while i<len(nums)-k+1:
            
            if nums[i] < 0:
                return False
            j = i
            n = nums[i]
            while j < i+k and j < len(nums):
                nums[j] = nums[j] - n
                
                j += 1
            while i<len(nums)-k+1 and nums[i]==0:
                i += 1
            # i += 1
        for i in range(len(nums)-1, len(nums)-k-1, -1):
            if nums[i]:
                return False
        return True