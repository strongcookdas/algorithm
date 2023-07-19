def dfs(L, n, k, p):
    if L == k:
        for x in p:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            p.append(i)
            dfs(L+1, n, k, p)
            p.pop()


def solution(n, k):
    dfs(0, n, k, [])
    return 'end'


print(solution(3, 2))
