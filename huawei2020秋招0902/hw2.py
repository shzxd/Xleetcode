def dfs(matrix, i, j):
    if i < 0 or j < 0 or i >= M or j >= N or matrix[i][j] != 'S':
        return
    matrix[i][j] = "H"
    dfs(matrix, i+1, j)
    dfs(matrix, i-1, j)
    dfs(matrix, i, j+1)
    dfs(matrix, i, j-1)

def solution(matrix):
    if matrix is None:
        return 0
    index = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 'S':
                dfs(matrix, i, j)
                index += 1
    return index

if __name__ == '__main__':
    M, N = map(int, input().split(','))
    matrix = [0]*M
    for i in range(M):
        matrix[i] = list(input())
    print(solution(matrix))