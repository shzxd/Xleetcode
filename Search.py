from typing import List


# 查找算法

# 二分查找
def binsearch(nums: List[int], target: int) -> int:
    """输入数组，以及要查找的值，返回索引，没找到返回-1"""
    nums.sort()
    i, j = 0, len(nums)-1
    import math
    while i <= j:
        mid = math.floor(i / 2 + j / 2)
        if target < nums[mid]:
            j = mid - 1
        elif target > nums[mid]:
            i = mid + 1
        else:
            return mid
    return -1