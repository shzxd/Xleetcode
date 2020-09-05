# 拼多多笔试题
# 打印"大风车"

def matrixfengche(n):
    if n < 4 or n > 199:
        return None
    if n % 2 == 0:
        mid = n // 2 - 0.01
    else:
        mid = (n - 1) // 2
    # print(mid)
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            # 左半边
            if i < mid:
                if j < mid:
                # 上半边
                # i: 0, 1
                # j: 0, 1
                    if i > j:
                        ans[j][i] = 2
                    elif i < j:
                        ans[j][i] = 3
                elif j > mid:
                # 下半边
                # j: 2, 3
                    if i + j < n - 1:
                        ans[j][i] = 4
                    if i + j > n - 1:
                        ans[j][i] = 5
            # 右半边
            elif i > mid:
                # 上半边
                if j < mid:
                    if i + j < n - 1:
                        ans[j][i] = 1
                    if i + j > n - 1:
                        ans[j][i] = 8
                # 下半边
                elif j > mid:
                    if i > j:
                        ans[j][i] = 7
                    elif i < j:
                        ans[j][i] = 6
    return ans
a = matrixfengche(16)
for i in a:
    for j in i:
        print(j, end=' ')
    print()
