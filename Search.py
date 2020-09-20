from typing import List


# 查找算法

# 二分查找
def binary_search(nums: List[int], target: int) -> int:
    """输入数组，以及要查找的值，返回索引，没找到返回-1"""
    nums.sort()
    i, j = 0, len(nums) - 1
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


# 美团一面: 给定数组, 元素先从小到大又从大到小排列, 找出最大元素
# 二分, 终止条件: 最大元素同时不小于左右两边

# https://www.geeksforgeeks.org/find-the-missing-number-in-a-sorted-array/?ref=rp
# 给定自然数数组, 数组中存在一个缺失元素, 寻找其中缺失的一个元素
# A binary search based program to find
# the only missing number in a sorted
# in a sorted array of distinct elements
# within limited range
def search(ar, size):
    a = 0
    b = size - 1
    mid = 0
    while b > a + 1:
        mid = (a + b) // 2
        if (ar[a] - a) != (ar[mid] - mid):
            b = mid
        elif (ar[b] - b) != (ar[mid] - mid):
            a = mid
    return ar[mid] + 1
