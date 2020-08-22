# 刷题常见输入输出

# 1.
# 输入: 输入包含多组测试数据，每一行包含两个整数 a 和 b
# 输出: 在一行中输出 a + b 的值
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except Exception as e:
        break

# 2.
# 输入： 输入第一行包括一个数据组数t(1 <= t <= 100)
#       接下来每行包括两个正整数a,b(1 <= a, b <= 10^9)
# 输出：　输出a+b的结果

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a + b)

# 3.
# 输入： 输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入
# 输出： 输出a+b的结果
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)

# 4.
# 输入：
# 输出：
while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break
    else:
        print(sum(line[1:]))

# 5.
# 输入： 输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
#       接下来t行, 每行一组数据。
#       每行的第一个整数为整数的个数n(1 <= n <= 100)。
#       接下来n个正整数, 即需要求和的每个正整数。
# 输出： 每组数据输出求和的结果
N = int(input())
for i in range(N):
    line = list(map(int, input().split()))
    if line[0] != 0:
        print(sum(line[1:]))

# 6.
# 输入： 输入数据有多组, 每行表示一组输入数据。
#       每行的第一个整数为整数的个数n(1 <= n <= 100)。
#       接下来n个正整数, 即需要求和的每个正整数。
# 输出：
while True:
    try:
        line = list(map(int, input().split()))
        if line[0] != 0:
            print(sum(line[1:]))
    except Exception as e:
        break

# 7.
# 输入： 输入数据有多组, 每行表示一组输入数据。 每行不定有n个整数，空格隔开。(1 <= n <= 100)。
# 输出： 每组数据输出求和的结果
while True:
    try:
        line = list(map(int, input().split()))
        print(sum(line))
    except Exception as e:
        break

# 7.
# 输入： 输入有两行，第一行n 第二行是n个空格隔开的字符串
# 输出： 输出一行排序后的字符串，空格隔开，无结尾空格
N = int(input())
line = list(input().split())
# note:
# 这里是list的sort方法
# key 指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如 key=str.lower)。
# 对应于列表中每一项的键会被计算一次，然后在整个排序过程中使用。
# 默认值 None 表示直接对列表项排序而不计算一个单独的键值。
line.sort()
for s in line:
    print(s, end=' ')

# ８.
# 输入： 多个测试用例，每个测试用例一行。 每行通过空格隔开，有n个字符，n＜100
# 输出： 对于每组测试用例，输出一行排序过的字符串，每个字符串通过空格隔开
while True:
    try:
        line = list(input().split())
        line.sort()
        for s in line:
            print(s, end=' ')
        print()
    except Exception as e:
        break

# 9.
# 输入： 多个测试用例，每个测试用例一行。 每行通过,隔开，有n个字符，n＜100
# 输出： 对于每组用例输出一行排序后的字符串，用','隔开，无结尾空格
while True:
    try:
        line = input().split(',')
        line.sort()
        # # 错误实现
        # for s in line:
        #     print(s, end=',')
        # note:
        # str.join(iterable) 返回一个由 iterable 中的字符串拼接而成的字符串。
        # 如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError。
        # 调用该方法的字符串将作为元素之间的分隔。
        print(','.join(line))
    except Exception as e:
        break

# 10.
# 输入： 输入有多组测试用例，每组空格隔开两个整数
# 输出： 对于每组数据输出一行两个整数的和
line = list(map(int, input().split()))
for i in range(0, len(line), 2):
    print(sum(line[i:i+2]))
