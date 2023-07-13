'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

q = [1]
visited = []

while q:
    current = q.pop(0)
    if current not in visited:
        visited.append(current)

    for destination in range(V+1):
        if (adj_matrix[current][destination] and destination not in visited):
            q.append(destination)

print('이동경로', visited)
