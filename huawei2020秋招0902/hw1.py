N = int(input())
# kids = [0]*N
d = {}
for i in range(N):
    d[tuple(map(int, input().split()))] = i + 1
print(d)
kids = list(d.keys())
kids1 = []
kids2 = []
for i in kids:
    if i[1] == 1:
        kids1.append(i)
    else:
        kids2.append(i)

kids1.sort()
kids2.sort()
sum1, sum2 = 0, 0
if len(kids1) >= 3:
    sum1 = kids1[-3][0] + kids1[-2][0] + kids1[-1][0]
if len(kids2) >= 3:
    sum2 = kids2[-3][0] + kids2[-2][0] + kids2[-1][0]

if sum1 > sum2:
    print(d[kids1[-3]], d[kids1[-2]], d[kids1[-1]])
    print(1)
    print(sum1)
elif sum1 < sum2:
    print(d[kids2[-3]], d[kids2[-2]], d[kids2[-1]])
    print(2)
    print(sum2)
else:
    print('null')
