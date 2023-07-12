# 프로그래머스 array 주차 요금 계산
# 걸린 시간 : 3 시간..
# 로직은 어렵지 않았지만 로직을 코드로 옮기는 과정에서 많은 오류가 있었다.
'''
IN일 경우
딕셔너리로 차량번호, 시간을 key - value 형식으로 저장
시간을 계산하는 딕셔너리에 차량번호 등록

OUT일 경우
해당 차량의 출입 시간을 조회한 후 시간 차이 계산 후 딕셔너리에 계산

계산된 시간 딕셔너리를 가지고 요금 계산후 반환

'''
import math


def solution(fees, records):
    answer = []
    car_in = {}
    car_time = {}

    for record in records:
        # print(record)
        record_lst = record.split(' ')
        if record_lst[2] == "IN":
            car_in[int(record_lst[1])] = record_lst[0]
            if int(record_lst[1]) not in car_time:
                car_time[int(record_lst[1])] = 0
        else:
            car_time[int(record_lst[1])
                     ] += cal_time(car_in[int(record_lst[1])], record_lst[0])
            del car_in[int(record_lst[1])]
        # print('car_time:', car_time)

    for key, value in car_in.items():
        car_time[key] += cal_time(car_in[key], "23:59")
        # print('car_time:', car_time)

    answer = cal_fee(car_time, fees)
    return answer


def cal_time(in_time, out_time):
    in_time_lst = in_time.split(":")
    out_time_lst = out_time.split(":")
    time = (int(out_time_lst[0]) * 60 + int(out_time_lst[1])
            ) - (int(in_time_lst[0]) * 60 + int(in_time_lst[1]))
    # print('time:', time)
    return time


def cal_fee(car_time, fees):
    answer = []
    sorted_car_time = dict(sorted(car_time.items()))
    for key, value in sorted_car_time.items():
        if value <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(math.ceil((value-fees[0])/fees[2])*fees[3]+fees[1])
        # print(answer)
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                                      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

# [14600, 34400, 5000]
