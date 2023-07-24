'''
greedy를 이용해서 문제를 해결
나가는 지점 오름차순으로 정렬
진입 지점이 나가는 지점보다 작으면 카메라 count 안한다.
'''


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cctv = -30001
    for start, end in routes:
        if start <= cctv:
            continue
        answer += 1
        cctv = end
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
