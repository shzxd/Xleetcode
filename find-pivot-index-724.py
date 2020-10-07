from typing import List


def pivotIndex(nums: List[int]) -> int:
    left, right = 0, sum(nums)
    for i in range(len(nums)):
        right -= nums
        if left == right:
            return i
        left += nums
    return -1