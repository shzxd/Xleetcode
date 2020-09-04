from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursive
        ans = []
        if root:
            ans.append(root.val)
            ans.extend(self.preorderTraversal(root.left))
            ans.extend(self.preorderTraversal(root.right))
        return ans

        # # Iteration
        # ans = []
        # stack = [root]
        # while stack:
        #     if root:
        #         ans.append(root.val)
        #         stack.append(root.right)
        #         root = root.left
        #     else:
        #         root = stack.pop()
        # return ans
