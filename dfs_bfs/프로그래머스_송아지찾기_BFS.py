'''
bfs 문제이다. (출발 상태에서 도착 상태까지의 최소 횟수 구하는 문제에 활용)
각 노드에서 -1, +1, +5 연산을 한다.
연산한 결과는 level+1의 level을 가진다.
level은 연산횟수를 의미한다.
연산한 결과가 이전의 노드에 있는 경우 큐에 넣지 않는다.
'''

from collections import deque

'''
시간 초과
def solution(s, e):
    q = [s]
    visited = [s]
    num_lst = [-1, 1, 5]
    answer = 0
    level = 0
    while q:
        q_length = len(q)
        for _ in range(q_length):
            num = q.pop(0)
            if num == e:
                answer = level
                return answer
            for i in num_lst:
                result = num + i
                if result not in visited:
                    q.append(result)
                    visited.append(result)
        level += 1


print(solution(5, 5))
'''

# 중요 ! 바운더리 체크해야 한다.


def solution(s, e):
    q = [s]
    visited = [0] * 10001
    visited[s] = 1
    num_lst = [-1, 1, 5]
    answer = 0
    level = 0
    while q:
        q_length = len(q)
        for _ in range(q_length):
            num = q.pop(0)
            if num == e:
                answer = level
                return answer
            for i in num_lst:
                result = num + i
                # 바운더리 체크 ***
                if result > 0 and result <= 10000 and visited[result] == 0:
                    q.append(result)
                    visited[result] = 1
        level += 1


print(solution(5, 18))
