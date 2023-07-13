# SW Expert Academy
# 7/12 오전 12시 시작
# 7/12 오전 2시 5분 완료 => 2시간
'''
N에 따라 2n-1번의 방향이 나타남 ex) n = 3일때, 5번의 방향이 나타난다. : for문으로 5번 반복문을 돈다. (방향 전환을 위해)
첫번째 반복문일때는 n번까지 직진 이동 : 이중 for문으로 n번 돌면서 숫자를 기록
이후부터 우,하 방향 좌, 상 방향 끼리 같은 횟수의 직진 이동을 함 (우,하) -> (좌,상) 으로 전환할 때 직진이동 횟수는 1감소 : 첫번째 for문을 한번 다 돌면 이중 for문의 반복문 횟수를 감소시킨다.
이것을 이용한다.

'''
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
test_num = int(input())
test_cnt = 1


def snail(lst_num):
    x_idx, y_idx = 0, -1
    count = 2*lst_num - 1
    count2 = lst_num
    snail_arr = [[0 for j in range(lst_num)] for i in range(lst_num)]
    cnt = 1
    for i in range(count):
        r, c = dir[i % 4]
        if i % 4 == 1 or i % 4 == 3:
            count2 -= 1
        # print('count2', count2)
        for j in range(count2):
            x_idx += r
            y_idx += c
            # print('x_idx', x_idx, 'y_idx', y_idx)
            # print('r', r, 'c', c)
            # print('cnt', cnt)
            snail_arr[x_idx][y_idx] = cnt
            cnt += 1

    # 프린트
    for i in range(lst_num):
        for j in range(lst_num):
            print(snail_arr[i][j], end=" ")
        print()


while test_cnt <= test_num:
    lst_num = int(input())
    print(f'#{test_cnt}')
    snail(lst_num)
    test_cnt += 1
