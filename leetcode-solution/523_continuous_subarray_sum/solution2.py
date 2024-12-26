from collections import defaultdict
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Bruteforce
        # create every subarray and check madi
        # prefix sum map
        ps_map = defaultdict(int)
        # prefix_sum
        ps_map[0] = -1 # 0 is sum till nothing is selected
        ps = 0

        for i, n in enumerate(nums):
            ps += n
            
            if k!=0:
                 # we're looking for sum multiples of k
                 # i.e. f*k will be sum of a sub array
                 # remainder will be ps - f*k i.e. ps%k
                 # If some subarray having remainder as their sum
                 # it means, current subarray has multiples of k
                ps %= k
            if ps in ps_map:
                # if length of subarray is at least 2 as per the given condition
                if i-ps_map[ps]>1:
                    return True
            else:
                # only update the first occurance 
                ps_map[ps] = i
        return False