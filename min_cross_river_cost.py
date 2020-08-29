from typing import List


def min_cross_river_cost(n: int, costs: List[int]) -> int:
    """输出N个人全部过河的时间，costs表示每个人的过河时间
    """
    # 时间从大到小排序
    costs.sort()
    t = 0
    i = n-1
    while i > 2:
        # 总策略：每次把最慢的两人运过去
        # 策略一：最快次快过河，最快回来，次慢最慢过河，次快回来
        # 2*costs[1] + costs[-1] + costs[0]
        t1 = 2*costs[1] + costs[i] + costs[0]
        # 策略2：最快最慢过河，最快回来，最快次慢过河，最快回来
        # 2*costs[0] + costs[-1] + costs[-2]
        t2 = 2*costs[0] + costs[i] + costs[i-1]
        if t1 < t2:
            t += t1
        else:
            t += t2
        i -= 2
    # 边界条件
    # 只剩3人
    if i == 2:
        t += sum(costs[:3])
    # 只剩2人
    elif i == 1:
        t += costs[1]
    # 只剩1人
    else:
        t += costs[0]
    return t

if __name__ == '__main__':
    N = int(input())
    costs = list(map(int, input().split()))
    print(min_cross_river_cost(N, costs))
