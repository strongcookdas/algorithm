# bfs 재귀적으로 푸는 방법에 대해서 고민 필요
# 푼 시간 40분

def dfs(S):

    global V

    visited.append(S)

    for des in range(V+1):
        if adj_matrix[S][des] == 1 and des not in visited:
            dfs(des)


def bfs(S):

    global V
    q = [S]

    while q:
        current = q.pop(0)
        if current in visited:
            continue
        visited.append(current)
        for des in range(V+1):
            if adj_matrix[current][des] == 1 and des not in visited:
                q.append(des)


V, E, S = map(int, input().split())
visited = []

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

dfs(S)
print(*visited)

visited.clear()

bfs(S)
print(*visited)
