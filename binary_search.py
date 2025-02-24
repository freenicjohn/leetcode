nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#       s           m           e

def binary_search(nums, target):
    s = 0
    e = len(nums) - 1
    while s <= e:
        m = (s + e) // 2
        if nums[m] == target: 
            return m
        elif target > nums[m]:
            s = m+1
        else:
            e = m-1
    
    return -1

if __name__ == "__main__":
    print(binary_search(nums, 3))  # 5
    print(binary_search(nums, 10))  # -1