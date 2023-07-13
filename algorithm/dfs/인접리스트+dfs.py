
V, E = map(int, input().split())

# 인접행렬
adj_matrix = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start].append(end)
    adj_matrix[end].append(start)

# dfs
stack = [1]
visited = []

while stack:
    # 단계1 stack에서 pop 후 visited 체크
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    # 단계2 current 노드에서 갈 수 있는 노드 탐색 후 visited 체크 후 stack 추가
    for destination in adj_matrix[current]:
        if destination not in visited:
            stack.append(destination)

print('이동경로 :', visited)
