# http://codenong.com/cs106759968
# 假设农场种中成熟的母牛每年都会生 1 头小母牛，并且永远都不会死。
#  第一年有 1 只小母牛，从第二年开始，母牛开始生小母牛。
#  每只小母牛 3 年后成熟又可以生小母牛。给定整数 N，求N年后牛的数量。

# Recursive 版本
# f(n) = f(n-1) + f(n-3)
def sol1(n):
    if n < 4:
        return n
    return sol1(n-1) + sol(n-3)


# Iteration 版本
def sol(n: int) -> int:
    if n < 4:
        return n
    else:
        f1, f2, f3 = 1, 2, 3
        for i in range(n-3):
            f4 = f3 + f1
            f1 = f2
            f2 = f3
            f3 = f4
        return f4


if __name__ == '__main__':
    print(sol(int(input())))