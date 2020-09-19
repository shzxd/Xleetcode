# 最长回文子串 leetcode 5

# 中心扩展算法
def longestPalindrome(s: str) -> str:
    ans = ''
    for i in range(len(s)):
        sub1 = expandAroundCenter(s, i, i)
        sub2 = expandAroundCenter(s, i, i + 1)
        ans = max(ans, sub1, sub2, key=len)
    return ans


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


# todo: Manacher算法

print(longestPalindrome('babad'))
