def merge_sort(nums):
    if len(nums) > 1:
        # Split in half
        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]
        
        # Sort both halves
        merge_sort(left)
        merge_sort(right)

        # Merge both halves in an ordered way
        l = 0
        r = 0
        i = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                nums[i] = left[l]
                l += 1
            else:
                nums[i] = right[r]
                r += 1
            i += 1

        # Add any remaining elements
        if l < len(left):
            while i < len(nums):
                nums[i] = left[l]
                i += 1
                l += 1
        elif r < len(right):
            while i < len(nums):
                nums[i] = right[r]
                i += 1
                r += 1
        
    return nums


if __name__ == "__main__":
    print(merge_sort([9, 3, 2, 6, 7, 8, 1]))
    print(merge_sort([-1, 20, 15, -20, 11]))
    print(merge_sort([2]))