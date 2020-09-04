# 递归模板
# 考虑两个条件：终止条件(不再调用自己），递归条件(调用自己）
# call stack

# 要注意的三点：
# 不要人肉递归
# 找到最近重复子问题
# 数学归纳法

# 编写设计数组的递归函数时，终止条件通常是数组为空或者只包含一个元素。
import functools


def countdown(i):
    print(i)
    if i == 1:  # base case
        return
    else:  # recursive case
        countdown(i-1)


# 递归阶乘
def factorial(n):
    if n == 1:
        return 1  # base case
    return n * factorial(n-1)  # recursive case


# 递归爬楼梯
@functools.lru_cache(100)  # 缓存装饰器
def climbStairs(n):
    # base case
    if n == 1:
        return 1
    elif n == 2:
        return 2
    # recursive case
    return climbStairs(n-1) + climbStairs(n-2)


# 带状态的递归
# 递归生成合规括号
def generateParenthesis(n):
    def generate(p, left, right, ans=[]):
        # recursive case
        if left:
            generate(p+'(', left-1, right)
        if right > left:
            generate(p+')', left, right-1)
        # base case
        if not right:
            ans += p
        return ans
    return generate('', n, n)


# 带状态的递归
# 递归验证BST
def isValidBST(root):
    def valid(root, less, larger):
        # base case
        if root is None:
            return True
        if root.val <= less or root.val >= larger:
            return False
        # recursive case
        return valid(root.left, less, root.val) and valid(root.right,
                                                          root.val, larger)
    return valid(root, float('-inf'), float('inf'))

# 递归找出二叉树最大深度
def maxDepth(root):
    # base case
    if root is None:
        return 0
    # recursive case
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# 递归判断平衡二叉树
def isBanlance(root, l, r):
    # base case
    if root is None:
        return True
    # recursive case
    if root.left:
        l += 1
    elif root.right:
        r += 1
    if l - r <= 1:
        return True
    else:
        return isBanlance(root.left, l, r) and isBanlance(root.right, l, r)


if __name__ == '__main__':
    print(climbStairs(38))