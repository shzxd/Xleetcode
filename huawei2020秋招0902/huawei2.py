# leetcode 130

def sol(nums):
    if not nums:
        return
    n, m = len(nums), len(nums[0])
    def dfs(x, y):
        if not 0 <= x < n or not 0 <= y <m or nums[x][y] != 'O':
            return
        nums[x][y] = 'A'
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
    for i in range(n):
        dfs(i, 0)
        dfs(i, m-1)
    for i in range(m-1):
        dfs(0, i)
        dfs(n-1, i)
    for i in range(n):
        for j in range(m):
            if nums[i][j] == 'A':
                nums[i][j] = 'O'
            elif nums[i][j] == 'O':
                nums[i][j] = 'X'
if __name__ == '__main__':
    nums = [['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'O', 'X']]
    sol(nums)
    for i in nums:
        print(i)