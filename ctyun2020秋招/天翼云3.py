# leetcode 198

def solution(nums):
    old, new = 0, 0
    for i in nums:
        if i < 0:
            continue
        old, new = new, max(old+i, new)
    return new

if __name__ == "__main__":
    nums = list(map(int, input().split(',')))
    print(solution(nums))