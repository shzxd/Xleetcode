# leetcode 1004
# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC
# %2B%2BPython-Sliding-Window

# @param arr int整型一维数组
# @param k int整型 允许0变为1的个数
# @return int整型
#
class Solution:
    def GetMaxConsecutiveOnes(self , arr , k ):
        # write code here
        i = 0
        for j in range(len(arr)):
            k -= 1 - arr[j]  # if arr[i] == 0: k -= 1
            if k < 0:
                k += 1 - arr[i]
                i += 1
        return j - i + 1