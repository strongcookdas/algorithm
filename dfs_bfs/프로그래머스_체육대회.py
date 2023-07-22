'''
dfs를 활용한 순열문제
'''
answer = 0
check = []


def dfs(ability, check, sum, depth):
    global answer

    if depth == len(ability[0]):
        answer = max(answer, sum)
        return

    for i in range(len(ability)):
        if check[i] == 0:
            check[i] = 1
            dfs(ability, check, sum+ability[i][depth], depth+1)
            check[i] = 0


def solution(ability):
    check = [0] * len(ability)
    dfs(ability, check, 0, 0)
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [
      30, 30, 30], [70, 0, 70], [100, 100, 100]]))
