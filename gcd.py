# Greatest Common Divisor (GCD)
# 欧几里得算法（辗转相除法）： 计算两个非负整数 a, b 的最大公约数
# 原理： gcd(a, b) = gcd(b, a mod b) 假设 a > b, a mod b != 0
# 以除数和余数反复做除法运算，当余数为 0 时，取当前算式除数为最大公约数

def gcd(a: int, b: int) -> int:
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
    # while b != 0:
    #     a, b = b, a % b
    # return a


g = gcd(12, 36)
print(g)
