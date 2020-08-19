class Solution:
    def isValid(self, s: str) -> bool:
        """具有最近相关性的问题，使用stack。
        """
        # 构建匹配项
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in dic:
                # 入栈的是相匹配的括号，这样出栈时直接判断相等即可
                # 也可以直接入栈，出栈时判断是否匹配。
                # 都一样，这里主要是区分相等与匹配
                stack.append(dic[c])
            elif c in dic.values():
                if (stack == []) or (c != stack.pop()):
                    return False
        # 写法1
        return not len(stack)
        # # 写法2
        # return len(stack) == 0
        # # 写法3
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False

    def isValid(self, s: str) -> bool:
        """暴力法，循环替换匹配的括号组。
        """
        while '()' in s or '[]' in s or '{}' in s:
            if '()' in s:
                s = s.replace('()', '')
            elif '[]' in s:
                s = s.replace('[]', '')
            elif '{}' in s:
                s = s.replace('{}', '')
        return not s