from functools import reduce
from typing import List
# 与subsets 78一样的思路

# 本想用数位映射的思路，但是7，8两数字表示4位字母，所有数位状态不统一
# 另：数位映射法二进制时代码比较简洁，设计其它进制需要自己转换，还要注意补足数位，所以并不合适。

def letterCombinations(digits: str) -> List[str]:
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
         '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # """Recursive"""
    # # base case
    # if len(digits) == 0:
    #     return []
    # if len(digits) == 1:
    #     return list(d[digits[0]])
    # # recursive case
    # # 此处与subsets78 一样的思路
    # # 假设前n-1个数字已经生成好答案，只需将最后一个数字分别附加
    # ans = letterCombinations(digits[:-1])
    # tail = d[digits[-1]]
    # return [sub + t for sub in ans for t in tail]

    """Iteration"""
    # 回溯：为了缩小问题规模，通过逐步构造问题的备选解，并在确定某一部分备选解不可能被
    # 补全为有效解时立即放弃（backtrack)该备选解
    # 在本题目中由于所有候选解都可以补全为有效解，因此可以说是回溯解法
    # 或者更简单的理解就是一种暴力穷举算法。
    if digits == '':
        return []
    return reduce(lambda ans, n: [sub + e for sub in ans for e in d[n]],
                  digits, [''])



if __name__ == '__main__':
    digits = '23'
    print(letterCombinations(digits))
