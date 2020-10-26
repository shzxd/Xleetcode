# Breadth-first search
# 只不过这里，放入搜索队列待遍历的元素也是一个队列（每层元素的队列）

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrder(root: TreeNode) -> list[list[int]]:
    if root is None:
        return []
    ans, level = [], [root]
    while level:
        ans.append([n.val for n in level])
        level = [leaf for n in level for leaf in (n.left, n.right) if leaf]
    return ans
