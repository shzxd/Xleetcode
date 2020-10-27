# 棘手之处在于，题中的数据关系没有以图的方式厘清后给出，而是原始状态
# 所以bfs过程中要维护一个临时图结构（仅有两个顶点，一条边），以及当前的路径长度
# 如果先根据题意将基因序列间的关系建立一个图，然后再进行bfs就很明了了
# 这跟最短路径问题几乎一样
from collections import deque


def minMutation(start: str, end: str, bank: list[str]) -> int:
    bank = set(bank)
    # queue中存放的是当前位置（基因串）以及当前状态步数
    # bfs中的逻辑为：验证当前状态（位置+步数）可达的位置并更新状态（位置+步数）后放入搜索队列
    queue = deque([(start, 0)])
    def isreachable(start, end):
        # d = 0
        # for i in range(8):
        #     if start[i] != end[i]:
        #         d += 1
        #         if d > 1:
        #             return False
        # return True
        return sum(start[i] != end[i] for i in range(8)) == 1
    while queue:
        tmp = queue.popleft()
        if tmp[0] == end:
            return tmp[1]
        bank.discard(tmp[0])
        for e in bank:
            if isreachable(tmp[0], e):
                queue.append((e, tmp[1]+1))
    return -1


if __name__ == '__main__':
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(minMutation(start, end, bank))