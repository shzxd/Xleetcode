# leetcode 3 无重复字符的最长子串

def lengthofLongestSubstring(s):
    maxlen = 0
    start = 0
    checked = {}

    for i in range(len(s)):
        if s[i] in checked and start <= checked[s[i]]:
            start = checked[s[i]] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        checked[s[i]] = i
    return maxlen
