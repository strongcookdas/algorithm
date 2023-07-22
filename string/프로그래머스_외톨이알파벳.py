'''
현재 문자와 이전 문자열 비교
    같으면 현재문자는 카운트 x
    다르면 현재문자는 카운트 o
딕셔너리 사용
'''

'''
통과했지만 가독정 x
def solution(input_string):
    answer = ''
    char_dict = {}
    for i in range(len(input_string)):
        cur = i
        pre = i-1
        if pre < 0:
            char_dict.setdefault(input_string[cur], 1)
            continue
        if input_string[cur] == input_string[pre]:
            continue
        char_dict.setdefault(input_string[cur], 0)
        char_dict[input_string[cur]] += 1

    print(char_dict)

    sorted_dict = dict(sorted(char_dict.items()))
    for key, value in sorted_dict.items():
        if value > 1:
            answer += key
    return answer if answer != "" else 'N' 


print(solution("edeaaabbccd"))
'''




import collections
def solution(input_string):
    answer = ''
    char_dict = collections.defaultdict(int)
    prev = None
    for cur in input_string:
        if cur != prev:
            char_dict[cur] += 1
        prev = cur
    for key, value in char_dict.items():
        if value > 1:
            answer += key
    return "".join(sorted(answer)) if answer != "" else 'N'


print(solution("edeaaabbccd"))
