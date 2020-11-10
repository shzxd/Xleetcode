# 从给定的三个排序数组中查找三个最接近的元素
# 2020米哈游招聘
# https://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/

def findclosed(num1: list, num2: list, num3: list) -> list:
    len1 = len(num1)
    len2 = len(num2)
    len3 = len(num3)
    ans1, ans2, ans3 = None, None, None
    # 最小值初始化为无限大
    mindiff = float('inf')
    # 初始遍历游标
    i, j, k = 0, 0, 0
    while (i < len1 and j < len2 and k < len3):
        # find min and max value of current
        minimum = min(num1[i], num2[j], num3[k])
        maximum = max(num1[i], num2[j], num3[k])
        # update ans
        if maximum - minimum < mindiff:
            ans1, ans2, ans3 = i, j, k
            mindiff = maximum - minimum
        #
        if mindiff == 0:
            break

        # update index 跟三数之和的思路相似
        if num1[i] == minimum:
            i += 1
        elif num2[j] == minimum:
            j += 1
        else:
            k += 1
    return [num1[ans1], num2[ans2], num3[ans3]]


if __name__ == '__main__':
    num1 = [1, 4, 10]
    num2 = [2, 15, 20]
    num3 = [10, 12]
    print(findclosed(num1, num2, num3))
