k = int(input())
n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

ans = [[0]*(k+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        ans[i][j] = ans[i-1][j]
        if j >= w[i-1] and ans[i][j] < ans[i-1][j - w[i-1]] + v[i-1]:
            ans[i][j] = ans[i-1][j - w[i-1]] + v[i-1]
print(ans[-1][-1])
