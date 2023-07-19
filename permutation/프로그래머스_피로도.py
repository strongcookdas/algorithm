# Lv2
# 프로그래머스 피로도
# dfs 순열
'''
재귀 사용
    최소 피로도가 임계값보다 작으면 통과
    던전 길이 비교하면서 max값 갱신
'''
answer = 0


def perm(k, depth, dungeons, check):
    global answer
    answer = max(answer, depth)

    if depth == len(dungeons):
        return

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and check[i] == 0:
            check[i] = 1
            perm(k-dungeons[i][1], depth+1, dungeons, check)
            check[i] = 0


def solution(k, dungeons):
    global answer
    perm(k, 0, dungeons, [0]*len(dungeons))
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
