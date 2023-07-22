'''
재귀를 활용
(3,5) 가 주어졌을 때 (3,4) -> (2,1) -> (1,0)
부모를 찾아 (1,0)까지 깊이 탐색을 한다.
부모가 RR일 경우
    RR 반환
부모가 Rr일 경우
    queries%4를 한 값에 대한 대응 유전자배열 반환
부모가 rr일 경우
    rr 반환
'''
query_lst = ["RR", "Rr", "Rr", "rr"]
generation = []


def recur_query(n, child):
    if n == 1:
        return 'Rr'

    query = recur_query(n-1, child//4)

    if query == 'Rr':
        return query_lst[child % 4]
    else:
        return query


def solution(queries):
    answer = []
    for n, child in queries:
        answer.append(recur_query(n, child-1))
    return answer


print(solution([[3, 1], [2, 3], [3, 9]]))
