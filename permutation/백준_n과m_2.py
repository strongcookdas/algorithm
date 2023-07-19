# 백준 n과 m(2)
# 걸린 시간 30분
N, M = map(int, input().split())

n_lst = list(range(1, N+1))
sel = [0] * M
check = [0] * N


def perm(depth, num):
    if depth == M:
        print(*sel)
        return

    for i in range(N):
        if not check[i] and i > num:
            check[i] = 1
            sel[depth] = n_lst[i]
            perm(depth+1, i)
            check[i] = 0


perm(0, -1)
