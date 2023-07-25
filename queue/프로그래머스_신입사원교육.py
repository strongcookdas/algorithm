import heapq


def solution(ability, number):
    answer = 0
    pQ = []

    for n in ability:
        heapq.heappush(pQ, n)

    for _ in range(number):
        a = heapq.heappop(pQ)
        b = heapq.heappop(pQ)
        heapq.heappush(pQ, a+b)
        heapq.heappush(pQ, a+b)

    while pQ:
        answer += heapq.heappop(pQ)

    return answer
