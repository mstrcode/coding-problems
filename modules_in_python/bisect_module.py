import bisect

# Sample sorted list
sorted_list = [1, 3, 4, 4, 7, 8, 9]

# Element to search for
element = 4

# Perform binary search using bisect_left
index = bisect.bisect_left(sorted_list, element)

print(index)


index = bisect.bisect_right(sorted_list, element)
print(index)
