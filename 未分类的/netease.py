# geeksforgeeks: count palindrome sub strings string

def sol(str):
    n = len(str)
    dp = [[0 for x in range(n)] for y in range(n)]
    F = [[False for x in range(n)] for y in range(n)]
    for i in range(n):
        F[i][i] = True
    for i in range(n-1):
        if str[i] == str[i+1]:
            F[i][i+1] = True
            dp[i][i+1] = 1
    for g in range(2, n):
        for i in range(n-g):
            j = g + i
            if str[i]==str[j] and F[i+1][j-1]:
                F[i][j] = True
            if F[i][j]:
                dp[i][j] = dp[i][j-1] + dp[i+1][j] + 1 - dp[i+1][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
    return dp[0][n-1]

if __name__ == '__main__':
    a = input()
    print(sol(a))
