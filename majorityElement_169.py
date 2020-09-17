# leetcode 169 多数元素

def majorityElement(nums):
    # 摩尔投票法
    votes = 0
    for num in nums:
        if votes == 0:
            ans = num
        if num == ans:
            votes += 1
        else:
            votes -= 1
    return ans
