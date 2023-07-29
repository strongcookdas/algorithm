'''
1로 이루어진 숫자를 나눠보고 0으로 떨어지는 숫자의 자릿수를 반환
필요한 데이터
    - 자릿수
'''


def solution():
    global n
    num = 1
    count = 1
    while num % n != 0:
        count += 1
        num *= 10
        num += 1
    print(count)


while True:
    try:
        n = int(input())
    except:
        break
    solution()
