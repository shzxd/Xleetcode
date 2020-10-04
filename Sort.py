# 选择排序 selection sort
# 1. 原地操作几乎是选择排序的唯一有点，但是适用的场景非常罕见
# 2. 选择排序交换次数比冒泡少一些，由于交换所需的CPU时间比比较所需的CPU时间多
# 因此，数组长度较小时，选择比冒泡快
# in-place
def selection_sort(nums):
    # 遍历元素
    for i in range(len(nums)-1):
        # 查找第i小的元素
        minindex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[minindex]:
                minindex = j
        # 交换元素
        if minindex != i:
            nums[i], nums[minindex] = nums[minindex], nums[i]
    return nums


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

if __name__ == '__main__':
    nums = [10, 7, 8, 9, 1, 5, 0]
    selection_sort(nums)
    print(nums)