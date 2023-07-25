'''
def solution(command):
    dir_lst = ['U', 'R', 'D', 'L']
    go = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
    back = {'U': (0, -1), 'R': (-1, 0), 'D': (0, 1), 'L': (1, 0)}
    answer = [0, 0]
    cur = 0
    for c in command:

        if c == 'G':
            x, y = go[dir_lst[cur]]
            answer[0] += x
            answer[1] += y
        elif c == 'B':
            x, y = back[dir_lst[cur]]
            answer[0] += x
            answer[1] += y
        elif c == 'R':
            cur += 1
            cur %= 4
        else:
            cur -= 1
            cur %= 4

    return answer


print(solution("GRGRGRB"))
'''

# 강의용


def solution(command):
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x = y = d = 0
    for c in command:
        if c == 'R':
            d = d(d+1) % 4
        elif c == 'L':
            d = (d-1) % 4
        elif c == 'G':
            x = x + dxy[d][0]
            y = y + dxy[d][1]
        elif c == 'B':
            x = x - dxy[d][0]
            y = y - dxy[d][0]
    return [x, y]
