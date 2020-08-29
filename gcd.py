# Greatest Common Divisor (GCD)
# 欧几里得算法（辗转相除法）： 计算两个非负整数 a, b 的最大公约数
# 原理： gcd(a, b) = gcd(b, a mod b) 假设 a > b, a mod b != 0
# 以除数和余数反复做除法运算，当余数为 0 时，取当前算式除数为最大公约数

def gcd(a: int, b: int) -> int:
    # # 辗转相除
    # while b != 0:
    #     r = a % b
    #     a = b
    #     b = r
    # return a

    # # Pythonic 写法
    # while b != 0:
    #     a, b = b, a % b
    # return a

    # 一个递归实现的减法版本
    # 减法视角：https://plumsempy.com/2020/08/24/gcd-and-the-magic-of-subtraction/
    if a == 0: return b
    if b == 0: return a
    return gcd(abs(a-b), min(a,b))

g = gcd(12, 36)
print(g)
