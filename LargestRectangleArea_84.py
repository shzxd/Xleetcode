from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """改进版-使用栈解决问题。

        用一个栈维护左边界索引，遍历寻找右边界，找到栈顶元素对应的右边界开始计算面积。
        利用栈的顺序性结合数据的顺序性（大小关系）。
        """
        ans = 0
        # 为初始元素创造左边界，注意： 栈中本来存的都是柱子索引以便为了后续计算“宽度”，这里直接存储-1是因为柱子高度既不会为-1同时，逻辑上索引0的左边界可以当做是-1
        stack = [-1]
        # 为末尾元素创造右边界，填入一个比可能的最小值还要小的元素，为了适配相等逻辑的判断
        heights.append(-1)

        # 开始遍历
        for i in range(len(heights)):
            # 这里的逻辑不能改写为 heights[i] < heights[stack[-1]]？？？
            while heights[i] < heights[stack[-1]]:
                ans = max(ans, heights[stack.pop()] * (i - stack[-1] - 1))
            # 这里暗含了等于的情况，原版对于相等时也是入栈的，这样在出栈时做了无谓的计算
            # 考虑栈中存储了多个高度相等的相邻的索引，对于这个高度，依次出栈的元素都不能是
            # 最大值，因为宽度差还没拉满，直到这组相邻索引的最后一个出栈才算出这块高度想等的柱型
            # 的最大矩形面积
            # 优化点就是大于时才存储新高度的索引，相等时只需更新索引即可。 即连续相等时，
            # 只存储最右侧索引
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                stack[-1] = i
        # 将开始添加的自定义值删除。虽然没用，但算是一个好习惯
        heights.pop()
        return ans

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     """使用栈解决问题。
    #
    #     用一个栈维护左边界索引，遍历寻找右边界，找到栈顶元素对应的右边界开始计算面积。
    #     利用栈的顺序性结合数据的顺序性（大小关系）。
    #     """
    #     ans = 0
    #     # 为初始元素创造左边界，注意： 栈中本来存的都是柱子索引以便为了后续计算“宽度”，这里直接存储-1是因为柱子高度既不会为-1同时，逻辑上索引0的左边界可以当做是-1
    #     stack = [-1]
    #     # 为末尾元素创造右边界，这里填0是因为柱子高度最小为0，只要不比最小的大就行
    #     heights.append(0)
    #
    #     # 开始遍历
    #     for i in range(len(heights)):
    #         # 这里的逻辑不能改写为 heights[i] < heights[stack[-1]]？？？
    #         while heights[i] < heights[stack[-1]]:
    #             ans = max(ans, heights[stack.pop()] * (i - stack[-1] - 1))
    #         # 这里暗含了等于的情况
    #         stack.append(i)
    #     # 将开始添加的自定义值删除。虽然没用，但算是一个好习惯
    #     heights.pop()
    #     return ans

    # def largestRectangleArea(self, heights: List[int]) -> int:
    # # 暴力1，枚举矩形所有可能的宽（并滑动所有柱子高度）
    # # 超时
    # ans = 0
    # for i in range(len(heights)):
    #     min_height = heights[i]
    #     for j in range(i, len(heights)):
    #         min_height = min(min_height, heights[j])
    #         ans = max(ans, min_height * (j - i + 1))
    # return ans

    # # 暴力2，枚举矩形所有可能的高（即每一个数组元素，并确定其所有可能宽度）
    # # 超时
    # ans = 0
    # for i in range(len(heights)):
    #     h = heights[i]
    #     left = i - 1
    #     right = i + 1
    #     while left >= 0 and heights[left] >= h:
    #         left -= 1
    #     while right < len(heights) and heights[right] >= h:
    #         right += 1
    #     ans = max(ans, h*(right-left-1))
    # return ans


# test cases
bars1 = [0, 1, 0, 1]
bars2 = [0, 9]
print(Solution.largestRectangleArea(Solution, bars1))