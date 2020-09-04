# 螺旋矩阵, leetcodes 54
# https://leetcode.com/problems/spiral-matrix/discuss/20579/Simple-Python-solution-by-mutating-the-matrix

# @param matrix int整型二维数组
# @return int整型一维数组
#
class Solution:
    def SpiralMatrix(self , matrix ):
        # write code here
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:
                for r in matrix:
                    ans.append(r.pop())
            if matrix:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for r in matrix[::-1]:
                    ans.append(r.pop(0))
        return ans