# leetcode 1109
# 记录区间起始状态的变化，最后用一个loop迭代计算当前时刻的状态
 

def sol(bookings, n):
    ans = [0] * (n + 1)
    for i, j, k in bookings:
        # 第i站上车k人
        ans[i-1] += k
        # 第j+1站下车k人
        ans[j] -= k
    for i in range(1, n):
        # 当前车上的人=前一站车上的人+当前车站的变化数
        ans[i] += ans[i-1]
    return ans[:-1]

