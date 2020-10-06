# 相似题有许多，经典回溯问题
# https://www.geeksforgeeks.org/top-20-backtracking-algorithm-interview-questions/

import itertools
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """1. 数位映射

    对于nums的每个元素，有两种状态选中或不被选中，映射到二进制的1或0
    则共有2^n种情况，n为元素个数
    """
    ans = []
    # 枚举2^n种情况
    for i in range(1 << len(nums)):
        subset = []
        # 根据n个数位状态生成子集
        for j in range(len(nums)):
            if i & 1 << j:
                subset.append(nums[j])
        # print(subset, bin(i))
        ans.append(subset)
    return ans

    # """2. Iteration"""
    # # 初始状态是空集
    # ans = [[]]
    # # 遍历每个元素，将该元素添加到结果中的每一个形成新的子集
    # # 并将新的子集集和并入结果
    # for i in nums:
    #     ans += [subset + [i] for subset in ans]
    #     # print(ans)
    # return ans
    # # # one line
    # # return reduce(lambda ans, i: ans + [subset + [i] for subset in ans],
    # #               nums, [[]])

    # # """3. Recursive"""
    # # 直接递归，写递归代码时将当前代码想像为一层的逻辑
    # # base case 当前层是否要终止？
    # if len(nums) == 0:
    #     return [[]]
    # # recursive case 当前层的逻辑处理
    # ans = subsets(nums[1:])  # 当前层答案依赖于下一层，即假设除了第一个元素，后面的都已排好
    # # 把nums[0]拎出来可以省一些内存空间，todo: 分析原因
    # # head = [nums[0]]
    # # ans += [subset + head for subset in ans]
    # # 得到当前层答案，将排好的结果分别加上第一个元素产生新子集附加在答案里
    # ans += [subset + [nums[0]] for subset in ans]
    # # print(ans)
    # return ans  # 返回答案
    # # note: 不要写成 return ans.extend([subset + [nums[0]] for subset in ans])
    # # 因为 list.extend(iterable) 返回 None，相当于写成了 return None

    # # 定义辅助函数 helper
    # # todo: 讲不明白，没有第一种直接递归写法明晰，或者暂时不理解。
    # def helper(nums, subset, ans):
    #     # print(subset)
    #     ans.append(subset)
    #     for i in range(len(nums)):
    #         # note: 第二个参数不要自作聪明写成 subset.append(nums[i])
    #         # 因为 list.append(item) 返回值是 None
    #         helper(nums[i+1:], subset+[nums[i]], ans)
    # ans = []
    # helper(nums, [], ans)
    # return ans

    # """4. 库函数"""
    # ans = []
    # # 对所有可能情况：从输入中选 0~n 个 遍历，直接使用组合函数得出每种可能的结果附加在答案里
    # for i in range(len(nums)+1):
    #     for j in itertools.combinations(nums, i):
    #         ans.append(j)
    # return ans
    # # # one line
    # # return [j for i in range(len(nums)+1) for j in itertools.combinations(nums,
    # #                                                                     i)]

    """5. 回溯 backtracking"""
    # todo: 似乎用到了DFS, BFS，待后续补充


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets(nums))
