'''
리스트를 셋으로 변환하여 원소 몇개있는지 확인
2중 for문 돌면서 확인
투포인터 사용
'''

'''
효율성 문제에서 통과하지 못함

def solution(gems):
    gems_count = len(set(gems))
    answer = []
    while gems_count <= len(gems):
        for i in range(len(gems)-gems_count+1):
            l_idx = i
            r_idx = gems_count-1 + i
            print(l_idx, r_idx)
            gems_set = set()
            while l_idx <= r_idx:
                gems_set.add(gems[l_idx])
                gems_set.add(gems[r_idx])
                l_idx += 1
                r_idx -= 1
                print('gems_set:', gems_set)
                print('gems_set_count', len(gems_set), 'count', gems_count)
            if (len(gems_set) == len(set(gems))):
                print('ok')
                answer.append(i+1)
                answer.append(gems_count+i)
                break
        if (len(answer) != 0):
            break
        gems_count += 1
    return answer
'''

'''
2) 딕셔너리 사용해서 두 포인터 활용 (검색 o)

필요한 것 
각 보석의 갯수를 카운트하는 딕셔너리
최소 index 카운트하는 변수
l_pointer, r_pointer

l_pointer, r_pointer를 둔다
l_pointer가 움직이는 조건:
    보석 카운트 딕셔너리의 key값이 모두 채워졌을 때 
    최소 index 수를 구하기 위한 포인터이다.
r_pointer가 움직이는 조건:
    보석 카운트 딕셔너리의 key값이 모두 채워지지 않았을 때
    모든 보석을 수집하기 위한 포인터이다.
'''

'''
def solution(gems):
    gems_count = len(set(gems))
    gems_dict = {gems[0]: 1}
    l_pointer = 0
    r_pointer = 0
    answer = [0, len(gems)]

    while l_pointer < len(gems) and r_pointer < len(gems):
        if len(gems_dict) == gems_count:
            if r_pointer - l_pointer < answer[1] - answer[0]:
                answer = [l_pointer, r_pointer]
            else:
                gems_dict[gems[l_pointer]] -= 1
                if gems_dict[gems[l_pointer]] == 0:
                    del gems_dict[gems[l_pointer]]
                l_pointer += 1
        else:
            r_pointer += 1
            if r_pointer == len(gems):
                break

            if gems[r_pointer] in gems_dict:
                gems_dict[gems[r_pointer]] += 1

            else:
                gems_dict[gems[r_pointer]] = 1

    answer = [answer[0]+1, answer[1]+1]
    return answer


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
'''
# 강의 답안




import collections
def solution(gems):
    answer = [0, 0]
    sH = collections.defaultdict(int)
    k = len(set(gems))
    lt = 0
    maxL = 10000000
    for rt in range(len(gems)):
        sH[gems[rt]] += 1
        while (len(sH) == k):
            if rt-lt+1 < maxL:
                maxL = rt-lt+1
                answer[lt+1, rt+1]
            sH[gems[lt]] -= 1
            if sH[gems[lt]] == 0:
                del sH[gems[lt]]
            lt += 1
    return answer
