# a b c d 均为0~9的数字, 求满足下式所有的可能取值
# abcd + bcda = 8888

def solution():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    abcd = a*1000 + b*100 + c*10 + d
                    bcda = b * 1000 + c * 100 + d * 10 + a
                    if abcd + bcda == 8888:
                        print(a, b, c, d)


if __name__ == "__main__":
    solution()