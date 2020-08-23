import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. 使用内置counter对象
        return collections.Counter(s) == collections.Counter(t)

        # # 2. 手工统计字符频率
        # freq = [0]*26
        # for i in s:
        #     freq[ord(i)-ord('a')] += 1
        # for i in t:
        #     freq[ord(i)-ord('a')] -= 1
        # 写法1
        # for i in range(26):
        #     if freq[i] != 0:
        #         return False
        # return True
        # 写法2
        # return freq == [0]*26
        # 写法3
        # return not any(freq)

        # # 3. one dict
        # freq = {}
        # for i in s:
        #     if i in freq:
        #         freq[i] += 1
        #     else:
        #         freq[i] = 1
        # for i in t:
        #     if i in freq:
        #         freq[i] -= 1
        #     else:
        #         return False
        # for i in freq.values():
        #     if i != 0:
        #         return False
        # return True

        # # 4. 词频统计，大小写敏感
        # ans = [s.count(c) == t.count(c) for c in string.ascii_lowercase]
        # return all(ans)

        # # 5. 直接sort后比较是否相等
        # return sorted(s) == sorted(t)
