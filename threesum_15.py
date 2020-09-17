def threesum(nums):
    N = len(nums)
    ans = []
    # 排序
    nums.sort()
    # 对数组中的元素遍历在其右侧寻找可能匹配的两个数
    for k in range(N-2):
        # 如果当前元素与上次重复就跳过
        if k > 0 and nums[k] == nums[k-1]:
            continue
        # 初始化右侧搜索的双游标
        i, j = k+1, N-1
        # 在右侧进行夹逼查找
        while i < j:
            # 当前状态
            s = nums[k] + nums[i] + nums[j]
            # 根据状态确定下一步
            if s < 0:
                # 和小了，移动左游标
                i += 1
                # 在满足游标条件的情况下，如果当前元素与前一次相同则跳过
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif s > 0:
                # 和大了，移动右游标
                j -= 1
                while j > i and nums[j] == nums[j+1]:
                    j -= 1
            else:
                # 搜索完成，准备输出以及更新游标
                ans.append([nums[k], nums[i], nums[j]])
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                j -= 1
                while j > i and nums[j] == nums[j+1]:
                    j -= 1
    return ans

