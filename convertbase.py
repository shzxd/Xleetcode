# 十进制转任意进制，base >= 2
def convertbase(num: int, base: int) -> str:
    if base < 2:
        return 'BaseError'
    if num == 0:
        return '0'
    ans = ''
    while num:
        num, r = divmod(num, base)
        ans = str(r) + ans
    return ans
