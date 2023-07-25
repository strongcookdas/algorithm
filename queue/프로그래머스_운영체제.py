'''
- 우선순위 큐가 활용된다.
- 모든 프로그램은 1부터 10까지 점수가 매겨짐
- 점수가 낮을수록 우선순위가 높은 프로그램
- 우선순위가 높은 프로그램을 먼저 실행
- 실행 중인 프로그램보다 우선순위가 높은 프로그램이 호출되어도 실행 중이던 프로그램은 중단x
- 우선순위가 같다면 먼저 호출된 프로그램이 먼저 실행된다.
'''

'''
실패
def solution(program):
    answer = [0] * 11
    program.sort(key=lambda x: (x[1]))
    print(program)
    cur = 0
    q = [program.pop(0)]
    while q:
        print('queue', q)
        excution = q.pop(0)
        wait = cur - excution[1] if cur != 0 else 0
        answer[excution[0]] += wait
        cur += excution[2]

        if len(program) != 0:
            while program[0][1] <= cur:
                print(program[0][1])
                temp = program.pop(0)
                print('len', len(program))
                q.append(temp)
                if len(program) == 0:
                    break
        q.sort(key=lambda x: (x[0]))
    answer[0] = cur
    return answer


print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
'''


'''
# 시간복잡도가 그닥 좋지 않다. 쓰레드 안정성 검사때문에
from queue import PriorityQueue
def solution(program):
    answer = [0]*10
    program.sort(key=lambda x: x[1])
    pQ = PriorityQueue()
    cur = 0

    def call_program():
        while len(program) > 0 and program[0][1] <= cur:
            pQ.put(program.pop(0))

    while len(program) > 0 or not pQ.empty():
        # 프로그램 종료시간 cur 이후 실행시킬 프로그램이 존재하지만 queue에 없는 경우가 있을 수도 있다.
        if pQ.empty():
            cur = program[0][1]
            call_program()
        excute = pQ.get()
        answer[excute[0] - 1] += (cur-excute[1])
        cur += excute[2]
        call_program()

    return [cur]+answer
'''

# 힙큐 사용, program.pop() 사용 자제




import heapq
def solution(program):
    answer = [0]*10
    n = len(program)
    program.sort(key=lambda x: x[1])
    pQ = []
    cur = 0
    pos = 0

    def call_program():
        nonlocal pos
        while pos < n and program[pos][1] <= cur:
            heapq.heappush(pQ, program[pos])
            pos += 1

    while pos < n or len(pQ) > 0:
        # 프로그램 종료시간 cur 이후 실행시킬 프로그램이 존재하지만 queue에 없는 경우가 있을 수도 있다.
        if len(pQ) == 0:
            cur = program[pos][1]
            call_program()
        excute = heapq.heappop(pQ)
        answer[excute[0] - 1] += (cur-excute[1])
        cur += excute[2]
        call_program()

    return [cur]+answer
