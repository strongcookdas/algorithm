# dfs 재귀함수
def dfs(n):
    if n not in visited:
        visited.append(n)

    for destination in range(V+1):
        if adj_matrix[n][destination] and destination not in visited:
            dfs(destination)


# 인접행렬
V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

visited = []

dfs(1)

# 경로 출력
print('이동 경로:', visited)
