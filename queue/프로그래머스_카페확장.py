'''
import math


def solution(menu, order, k):
    answer = 0
    q = [order[0]]
    p = 0
    p2 = 1
    c = menu[order[p]]
    print('c', c)
    t = k
    while p < len(order):
        print(c, t)
        if c > t:
            if p2 < len(order):
                q.append(order[p2])
                p2 += 1
                answer = max(answer, len(q))
                t += k
        elif c == t:
            if len(q) > 0:
                q.pop(0)
                p += 1
                c = menu[order[p]]
            if p2 < len(order):
                q.append(order[p2])
                p2 += 1
            t = k
        else:
            if len(q) > 0:
                q.pop(0)
                c += menu[order[p]]
    return answer


print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))
'''

from collections import deque


def solution(menu, order, k):
    answer = 0
    queue = deque()
    complete = -1
    idx = 0
    for t in range(k * (len(order)-1)+1):
        if t == complete:
            queue.popleft()
            complete = -1
        if t == k*idx:
            queue.append(order[idx])
            idx += 1
            answer = max(answer, len(queue))
        if complete == -1 and len(queue) > 0:
            complete = t + menu[queue[0]]

    return answer
