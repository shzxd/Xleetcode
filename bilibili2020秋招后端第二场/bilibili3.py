# 字符串碎片 网易2018校招原题

#
# @param str string字符串
# @return int整型
#
class Solution:
    def GetFragment(self , str ):
        # write code here
        # 串总长度 // 相同字母构成的子串个数
        counter = 1 #  必须为1,防止空串出现除数为0的情况
        for i in range(0, len(str)-1):
            if str[i] != str[i+1]:
                counter += 1
        return len(str) // counter