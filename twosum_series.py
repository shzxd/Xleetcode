from typing import List


# two sum leetcode 01
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # # 暴力
    # for i in range(len(nums)-1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # hash
    dic = {}
    for i in range(len(nums)):
        if (target - nums[i]) in dic.keys():
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i

# three sum leetcode 15
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # 排序+三索引，逻辑很棒
    # nums从小到大排序
    # 用一个索引k遍历nums元素，用两个索引i,j在k右侧的数组中夹逼寻找满足题解的三数。
    # k遍历时 nums[k] > 0 直接跳过，nums[k] == nums[k-1]时跳过
    # i, j夹逼时，总和小于0移动左索引，大于0移动右索引，等于0记录该组解同时移动索引。
    #  在移动中注意要跳过相等的元素（k固定的情况下，再有一个元素相等，则这两组解重复）。
    #  在夹逼时注意终止条件 i >= j, 即while i < j时执行计算。

    ans = []
    nums.sort()
    N = len(nums)
    for k in range(N-2):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k-1]:
            continue
        i = k + 1
        j = N - 1
        while i < j:
            e = nums[i] + nums[j] + nums[k]
            if e < 0:
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1

            elif e > 0:
                j -= 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                j -= 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
    return ans
