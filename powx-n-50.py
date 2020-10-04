def myPow(x: float, n: int) -> float:
    """ D&c + Recursive"""

    # Base case
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)

    # Recursive case
    # divide problem，注意这里分治不是指奇偶性的分情况讨论，奇数分支最多只会运行一次
    # conquer
    # merge

    # # 易理解的版本
    # tmp = myPow(x, n//2)
    # if n % 2:
    #     return x * tmp * tmp
    # else:
    #     return tmp * tmp

    # 改进版
    if n % 2:  # or n & 1
        return x * myPow(x, n-1)
    else:
        return myPow(x*x, n//2)

    # # 错误写法及分析
    # # 1. 完全递归，没有分治，甚至递归都算不上
    # # 本来这里分治的核心就是复用之前幂计算的结果，
    # # 分解成相同的子问题，计算一个子问题答案然后合并答案为原问题的解。
    # # 如下写法依然做了重复的运算，与直接myPow(x, n)没有区别
    # return myPow(x, n//2) * myPow(x, n//2)
    #
    # # 2. 语言设计相关：平方运算与乘法运算没有产生一样的结果。
    # # IEEE 754 规定溢出时应返回无限大。
    # # (wikipedia:https://en.wikipedia.org/wiki/IEEE_754#Exception_handling)
    # # 在python中 x*x 溢出时遵循规定，但**运算或pow函数抛出异常overflowError
    # # eg. 计算表达式 x = 1e200, x*x, x**x, pow(x, 2)
    # return myPow(x, n//2) ** 2
    # # 或者
    # return myPow(x**2, n//2)

    # """Iteration"""
    # if n < 0:
    #     x = 1 / x
    #     n = -n
    # ans = 1
    # while n:
    #     if n % 2:
    #         ans *= x
    #     x *= x
    #     n //= 2  # or n >>= 1
    # return ans


if __name__ == '__main__':
    print(myPow(2.0, -2147483648))
