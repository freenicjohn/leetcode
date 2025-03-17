"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.

Examples:

Input: [1,3,5,6], 5
        l m   r
          l m r
         lm r
            l
Output: 2

Input: [1,3,5,6], 2
        l m   r
       lm r
          l 

Output: 1
"""

def search_insert_position(nums, target):
    l, r = 0, len(nums)-1

    while (l < r):
        m = (l + r) // 2

        if nums[m] >= target:
            r = m
        else:
            l = m+1

    return l

print(search_insert_position([1,3,5,6], 5))
print(search_insert_position([1,3,5,6], 2))
