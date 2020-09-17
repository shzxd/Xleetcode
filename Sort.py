# 快速排序 quicksort or 分区交换排序 partition-exchange sort
# 平均时间复杂度 O(nlogn)
# 最坏时间复杂度 O(n^2)
# 分治策略

# 原地版本 in-place
def partition(nums, left, right, pivotindex):
    pivot = nums[pivotindex]
    # 把pivot移到列尾
    nums[right], nums[pivotindex] = nums[pivotindex], nums[right]
    storeindex = left
    for i in range(left, right):
        if nums[i] <= pivot:
            # swap
            nums[storeindex], nums[i] = nums[i], nums[storeindex]
            storeindex += 1
    # 把列尾的pivot移回左右分区交接处 move pivot to storeindex
    nums[storeindex], nums[right] = nums[right], nums[storeindex]
    return storeindex


def quicksort(nums, left, right):
    if right > left:
        pivotnewindex = partition(nums, left, right, left)
        quicksort(nums, left, pivotnewindex-1)
        quicksort(nums, pivotnewindex+1, right)


nums = [10, 7, 8, 9, 1, 5, 0]
quicksort(nums, 0, len(nums)-1)
print(nums)