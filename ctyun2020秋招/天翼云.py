# leetcode 263

def solution(n):
    dp = [1]
    factor2, factor3, factor5 = 0, 0, 0
    while n > 1:
        n2, n3, n5 = dp[factor2]*2, dp[factor3] *3, dp[factor5]*5
        tmp = min(n2, n3, n5)
        if tmp == n2: factor2 += 1
        if tmp == n3: factor3 += 1
        if tmp == n5: factor5 += 1
        dp.append(tmp)
        n -= 1
    return dp[-1]

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(solution(n))
        except EOFError:
            break
