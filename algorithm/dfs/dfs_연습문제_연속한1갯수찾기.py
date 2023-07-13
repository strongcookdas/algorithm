# N*N크기의 배열이 주어졌을때 1의 개수는 몇개인지 세어보기 dfs를 이용해서
# 하나의 시작 1로 부터 붙어져 있는 연속된 1의 개수 세어보기 => 2, 13이 답이 됨.
'''
7
0000011
0000000
0011100
0010111
0110010
0011100
0000000
'''
# 방향잡기(상,우,하,좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# dfs


def dfs(r, c):
    global cnt

    arr[r][c] = 0
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if arr[nr][nc] == 0:
            continue

        dfs(nr, nc)


N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            print(cnt)
