from collections import deque


def solution(n, m, hole):
    answer = 0
    board = [[0 for _ in range(m+1)]for _ in range(n+1)]
    dist = [[[-1, -1] for _ in range(m+1)] for _ in range(n+1)]
    for x, y in hole:
        board[x][y] = 1
    queue = deque()
    queue.append((1, 1, 0))
    dist[1][1][0] = 0
    while len(queue) > 0:
        # cs 신발 사용했으면 1 아니면 0
        x, y, cs = queue.popleft()
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            for s in range(2):
                if cs == 1 and s == 1:
                    continue
                # 신발을 사용했을 경우 dx * 2
                nx, ny, ns = x + dx*(s+1), y + dy*(s+1), cs | s
                if nx < 1 or ny < 1 or nx > n or ny > m or board[nx][ny] > 0 or dist[nx][ny][ns] != -1:
                    continue
                queue.append((nx, ny, ns))
                dist[nx][ny][ns] = dist[x][y][cs] + 1
    answer = dist[n][m][1]
    if answer == -1 or (dist[n][m][0] >= 0 and dist[n][m][0] < answer):
        answer = dist[n][m][0]
    return answer


print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3],
      [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
