"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))
"""

# this is a very easy problem if you don't want to do it manually
# let's do it semi-manually by using .sort() but not .median()
# to check other cases just modify these. I'm just showing my solution so 
# I won't make a program to load in test cases.
nums1 = [1, 3, 4]
nums2 = [2, 5]

# lists can be concatenated and sorted easily in python, though this
# will raise your complexity from O(m+n) to O(log(m+n))
nums3 = nums1 + nums2
nums3.sort()
length = len(nums3)
# here you can see our sorted list
print(nums3)

# We need to tackle both the case that the list is even-len() or odd-len()
    # in some versions of python you don't need to force int() here
    # in leetcode for example it is not needed
if len(nums3) % 2 == 0:
    # if it's even-len() then we need to calculate median and it should be a float
    lowmed = nums3[int(length / 2) - 1]
    highmed = nums3[int(length / 2)]
    median = lowmed + float((highmed - lowmed)) / 2
    print("Median: ", median)
else:
    # len() returns an int which rounds up on division
    median = nums3[int((length / 2))]
    print("Median: ", median)