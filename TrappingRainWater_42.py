# 像 stack, queue, array 这类线性结构在使用时肯定也是为了利用它们的线性顺序特性，那么使用时
# 保持元素的大小关系肯定会更加的便利
# todo: 题解动态规划？
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 1. 双索引遍历，按列累加“雨水”
        # 边界条件
        if height is None or len(height) <= 2:
            return 0
        ans = 0
        left_h, right_h = height[0], height[-1]
        i, j = 1, len(height) - 2
        while i <= j:
            if left_h < right_h:
                if height[i] < left_h:
                    ans += left_h - height[i]
                else:
                    left_h = height[i]
                i += 1
            else:
                if height[j] < right_h:
                    ans += right_h - height[j]
                else:
                    right_h = height[j]
                j -= 1
        return ans

        # # 维护一个最小栈，固定一个右边界寻找相对这个右边界最大的左边界，这样找到一块解。
        # # 放在这道题里就是一个盛水的池子
        # if len(height) <= 2:
        #     return 0
        # stack = [0]
        # ans = 0
        # for i in range(1, len(height)):
        #     # 这里注意出栈计算时要始终保留栈中至少两个元素，这样，弹出一个后仍留有左边界
        #     while len(stack) >= 2 and height[i] > height[stack[-1]]:
        #         base = height[stack.pop()]
        #         h = min(height[i], height[stack[-1]])
        #         ans += (h - base) * (i - 1 - stack[-1])
        #     if height[i] < height[stack[-1]]:
        #         stack.append(i)
        #     else:
        #         stack[-1] = i
        # return ans