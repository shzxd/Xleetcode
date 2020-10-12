# 经典回溯：用这道题可以很直观的理解回溯的思想

# note: 皇后攻击范围：整行，整列，整条对角线
def solveNQueens(n: int) -> list[list[str]]:
    """回溯 backtracking"""
    def dfs(queens: list, left: set, right: set):
        # 将行作为递归层级
        row = len(queens) # 表示当前已经排好的皇后行数，即当前候选解
        # 如果当前已经排了n行皇后，说明该解是有效解
        if row == n:
            ans.append(queens)
            return
        # 遍历当前层的每一个位置，即每一列
        for col in range(n):
            # 当前放皇后的位置如果与已有皇后均不冲突则递归的行进
            # 规则：不在已有皇后的列，左对角线，右对角线上。
            # 因为按行递归，所以不会出现在已有皇后的行上
            if (col not in queens) and (col - row not in left) \
                    and (col + row not in right):
                dfs(queens+[col], left | {col-row}, right | {col+row})

    ans = []
    dfs([], set(), set())
    return [['.' * i + 'Q' + '.' * (n-i-1) for i in sub] for sub in ans]


if __name__ == '__main__':
    for sub in solveNQueens(4):
        for row in sub:
            print(row)
        print()
