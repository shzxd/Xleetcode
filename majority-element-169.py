import collections
# from random import random
import random
from functools import reduce
from typing import List

def majorityElement(nums: List[int]) -> int:
    # """使用字典对每个元素计数"""
    # d = dict.fromkeys(nums, 0)
    # for i in nums:
    #     d[i] += 1
    # # 也可在遍历中自己维护一个最大值：具有最大value的key
    # return max(d, key=d.get)

    # # 直接使用Counter容器
    # return collections.Counter(nums).most_common(1)[0][0]

    # """排序后返回中位数"""
    # return sorted(nums)[len(nums)//2]

    # """随机选择法"""
    # # 基于题中假设总是存在众数，因此随机选择一个元素进行验证，有很大概率命中
    # freq = len(nums) // 2
    # while True:
    #     # 随机选择序列中的一个元素
    #     ans = random.choice(nums)
    #     # 验证 sum(ans == i for i in nums)
    #     if nums.count(ans) > freq:
    #         return ans

    # """Divide & Conquer"""
    # # base case
    # if len(nums) == 1:
    #     return nums[0]
    # # D&C
    # lmode = majorityElement(nums[:len(nums)//2])
    # rmode = majorityElement(nums[len(nums)//2:])
    # # 合并子问题：if分支以及写在return中的逻辑
    # if lmode == rmode:
    #     return lmode
    # return lmode if nums.count(lmode) > (freq := len(nums) // 2) else rmode

    """摩尔投票法"""
    # 将目标值与其它值分别记为1和-1
    # 初始状态为0，目标值为空。
    # 遍历数组， 遇到目标值+1，非目标值-1
    # 如果状态为0，更新目标值。相当于之前遍历过的都扔掉不要了，因为为0，所以不影响。
    counter = 0
    ans = None
    for i in nums:
        if counter == 0:
            ans = i
        counter += 1 if i == ans else -1
    if counter > 0:
        return ans

    # 使用reduce或许更好理解摩尔投票的思想
    # ans = None
    # def slide(counter, i):
    #     nonlocal ans
    #     if counter == 0:
    #         ans = i
    #     counter += 1 if i == ans else -1
    #     return counter
    # if reduce(slide, nums, 0) > 0:
    #     return ans


if __name__ == '__main__':
    nums = [3, 4, 3]
    print(majorityElement(nums))