nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#       l     t     m           r

def binary_search(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        m = (l + r) // 2
        print(f"{l} {m} {r}")
        if nums[m] >= target:
            r = m
        else:
            l = m+1

    return l if nums[l] == target else -1

if __name__ == "__main__":
    print(binary_search(nums, 3))
    print(binary_search(nums, 10))
