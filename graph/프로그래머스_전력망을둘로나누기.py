import math

cnt = 0


def solution(n, wires):
    answer = 101
    global cnt
    wires_graph = [[]for _ in range(n+1)]
    # 인접 그래프
    for start, end in wires:
        wires_graph[start].append(end)
        wires_graph[end].append(start)

    # dfs 함수
    def dfs(v):
        global cnt
        visited[v] = 1
        cnt += 1
        for i in wires_graph[v]:
            if visited[i] == 0:
                dfs(i)

    # 탐색
    for start, end in wires:
        cnt = 0
        visited = [0] * (n+1)
        visited[end] = 1
        dfs(start)
        answer = min(answer, abs(cnt-(n-cnt)))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [
      4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
