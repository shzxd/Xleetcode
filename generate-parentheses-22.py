# 带状态的递归
# leetcode 22
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

# 以上思路也被认为是dfs
# 也有思路认为可以从bfs的角度来解题