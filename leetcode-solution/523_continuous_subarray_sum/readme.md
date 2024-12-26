## prefix sum properties
1. prefix_sum[i]: sum of first i elements in nums i.e. sum of [0,i-1] inclusive
2. prefix_sum[0] is 0 because, according to above description - nums 0 elements sum is 0
3. Most important visualization is: prefix_sum[higher]-prefix_sum[lower], where higher > lower and both < length of nums, is sum of subarray (lower: higher]
4. prefix_sum is actually powerful to tell sum of any subarray in O(1) time.