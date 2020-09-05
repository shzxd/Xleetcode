# 美团判断字符串是否合法

# n = int(input())
# T = input()

n = 10
T = "TTMMTTTEE"

# 判断合法
for i in range(n):
    if T[i] == 'M':
        break
# find start
start = i
for start in range(i+1, n):
    if T[start] == 'T':
        break
# 判断合法
for i in range(n):
    if T[i] == 'T':
        break
# find end
end = i
for end in range(i+1, n):
    if T[end] == 'M':
        break
if start > end:
    print(T)
else:
    print(T[start+1:end])

#
# ###############
# i = 0
# while T[i] != 'M' and i < n:
#     i += 1
# # find start
# j = i + 1
# while T[j] != 'T' and j < n:
#     j += 1
# # 判断合法
# m = n - 1
# while T[m] != 'T' and m > 0:
#     m += 1
# # find end
# n = m - 1
# while T[n] != 'M' and n > 0:
#     n += 1
# if j > n:
#     print(T)
# else:
#     print(T[j+1:n])
#
