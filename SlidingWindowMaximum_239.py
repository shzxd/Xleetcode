import collections
from typing import List
# 相似题：84

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """双端队列法就是暴力法的优化。

        可以尝试这样理解：在暴力法中抛弃了遍历过的元素的大小关系，每次滑动窗口重新判断最大值。
        优化点就在这里，不要抛弃历史元素的大小信息。我们通过维护一个数据结构，这个数据机构里存储的
        后续滑动窗口可能的最大值。
        凭直觉我们应该选一个具有顺序结构的（表征元素的先后顺序），方便我们维护大小关系的（增删查）
        这样一种数据结构，如果没有系统练习过各种数据结构，可能最先想到的就是数组。
        在数组基础上继续优化的话就能想到用队列了。
        """
        candidate = collections.deque(maxlen=k)
        ans = []
        for i, v in enumerate(nums):
            # 更新队列中的候选元素
            while candidate and v > nums[candidate[-1]]:
                candidate.pop()
            candidate.append(i)
            # 清除没有意义的最大值，最大值索引落后窗口的话再大也没用
            # 队列不存索引的话，这一步无法完成
            if candidate and candidate[0] <= i - k:
                candidate.popleft()
            # 输出每轮的结果
            if i >= k-1:
                ans.append(nums[candidate[0]])
        return ans

        # # 数组版本
        # # 窗口每滑动一次更新一次当前最大值，暴力方法的优化，同时记录最大值索引，
        # N = len(nums)
        # if N * k == 0: return []
        # if k == 1: return nums
        # window, ans = [], []
        # for i in range(N):
        #     # 队列满了弹出队尾，这里实际上不是队列满了，而是队尾最大值索引如果落后窗口的话，
        #     #  那么再大也没用，要弹掉
        #     if i >= k and window[0] <= i - k:
        #         window.pop(0)
        #     # 当前元素大于队尾元素，弹出队尾元素，新元素入队，这里比较大小用值，
        #     #  出入队用的是索引，以便第一步元素过期判断
        #     while window and nums[i] >= nums[window[-1]]:
        #         window.pop()
        #     window.append(i)
        #     if i > k - 2:
        #         ans.append(nums[window[0]])
        # return ans

        # """暴力。超时
        #
        # 两层loop，一个遍历所有窗口，一个遍历窗口内所有元素区最大值
        # time complexity: O(n*k)
        # """
        # # 原版
        # ans = []
        # for i in range(len(nums)-k+1):
        #     max_value = float('-inf')
        #     for j in range(k):
        #         if nums[i+j] > max_value:
        #             max_value = nums[i+j]
        #     ans.append(max_value)
        # return ans

        # # 改进版
        # ans = []
        # for i in range(len(nums)-k+1):
        #     ans.append(max(nums[i:i+k]))
        # return ans

        # # 题解版
        # n = len(nums)
        # # 为何要n * k，题中说了，n,k均不会为0
        # # 软件工程了，考虑下异常情况？做题的角度不需要，但是实际中，这样一个操作还是有必要的
        # # 同时这个 n * k == 0的逻辑判断很巧妙！
        # if n * k == 0:
        #     return []
        # return [max(nums[i:i+k]) for i in range(n-k+1)]

        # # 题解版缩减
        # return [max(nums[i:i+k]) for i in range(len(nums)-k+1)]


nums = [1, 3, 1, 2, 0, 5]
k = 3

nums = [4, -2]
k = 2

nums = [1, -1]
k = 1
print(Solution.maxSlidingWindow(Solution,nums,k))