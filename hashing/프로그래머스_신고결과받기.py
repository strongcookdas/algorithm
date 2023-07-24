# 프로그래머스 신고 결과 받기
# 시작 7/12 오전 9시
# 완료
'''
-> 이렇게 풀면 안된다. : 시간 초과
딕셔너리 생성
    유저 index
2차원 리스트 생성
    누가 누구를 신고했는지
유저가 신고할 때
    유저의 index를 찾는다.
    2차원 리스트에 신고 기록 체크
    신고당한 사람의 신고 횟수 카운트
    블랙리스트 처리시 결과 리스트에 메일 카운트
--------------------------------------------------------------------------
'''
''' 
시간 초과 코드
def solution(id_list, report, k):
    user_idx = {}
    idx = 0
    answer = [0 for i in range(len(id_list))]
    report_cnt = 0
    
    # 유저의 index 딕셔너리
    for user_id in id_list:
        user_idx[user_id]=idx
        idx+=1

    user_report_list = [[0 for j in range(len(id_list))] for i in range(len(id_list))]
    for r in report:
        reporter, black = tuple(r.split(' '))
        
        if user_report_list[user_idx.get(reporter)][user_idx.get(black)] != 0:
            continue
        
        user_report_list[user_idx.get(reporter)][user_idx.get(black)] = 1

        for i in range(len(id_list)):
            report_cnt+=user_report_list[i][user_idx.get(black)]

        print(report_cnt)
        if report_cnt == k:
            for i in range(len(id_list)):
                if(user_report_list[i][user_idx.get(black)]==1):
                    answer[i] += 1
        report_cnt = 0

    return answer
'''

'''
가독성이 안좋음
def solution(id_list, report, k):
    user_idx = {}
    user_report_count = {}
    idx = 0
    answer = [0 for i in range(len(id_list))]

    # 유저의 index 딕셔너리
    for user_id in id_list:
        user_idx[user_id] = idx
        user_report_count[user_id] = 0
        idx += 1

    user_report_list = [[0 for j in range(len(id_list))]
                        for i in range(len(id_list))]
    for r in report:
        reporter, black = tuple(r.split(' '))

        if user_report_list[user_idx.get(reporter)][user_idx.get(black)] != 0:
            continue

        user_report_list[user_idx.get(reporter)][user_idx.get(black)] = 1
        user_report_count[black] += 1

    for key, value in user_report_count.items():
        if (value >= k):
            for i in range(len(id_list)):
                if (user_report_list[i][user_idx.get(key)] == 1):
                    answer[i] += 1
    return answer
'''

# 강의 답안




import collections
def solution(id_list, report, k):
    answer = []
    # 중복 제거한다.
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    stoped = collections.defaultdict(int)

    for x in report:
        a, b = x.split(' ')
        reportHash[a].add(b)
        stoped[b] += 1

    for name in id_list:
        mail = 0
        for user in reportHash[name]:
            if stoped[user] >= k:
                mail += 1
        answer.append(mail)
    return answer
