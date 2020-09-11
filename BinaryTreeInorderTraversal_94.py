# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # # Recursive
        # ans = []
        # if root:
        #     ans.extend(self.inorderTraversal(root.left))
        #     ans.append(root.val)
        #     ans.extend(self.inorderTraversal(root.right))
        # return ans

        # Iteration
        ans = []
        stack = []
        while stack or root:
            # 遍历父节点直到没有左节点
            if root:
                stack.append(root)
                root = root.left
            else:
                # 此时将栈顶元素：父节点 弹出取值
                root = stack.pop()
                ans.append(root.val)
                # 迭代右节点
                root = root.right
        return ans