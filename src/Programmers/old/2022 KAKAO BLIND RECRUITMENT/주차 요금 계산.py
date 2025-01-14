"""
주차 요금 계산
https://programmers.co.kr/learn/courses/30/lessons/92341
"""


def decode_time(x):
    h = int(x[0:2]) * 60
    m = int(x[3:])
    return h + m


def get_time(a, b):
    if a / b > int(a / b):
        return int(a / b) + 1
    else:
        return int(a / b)


def solution(fees, records):
    end = decode_time("23:59")
    car_data = dict()

    for record in records:
        rtime, rcar, which = record.split()
        if rcar not in car_data:
            car_data[rcar] = [0 for _ in range(end)]

        if which == "IN":
            car_data[rcar][decode_time(rtime)] += 1
        else:
            car_data[rcar][decode_time(rtime)] -= 1

    for ck, cv in car_data.items():

        for i in range(end - 1):
            car_data[ck][i + 1] += car_data[ck][i]

        for i in range(end - 1):
            car_data[ck][i + 1] += car_data[ck][i]
        parking_time = car_data[ck][-1]
        car_data[ck] = fees[1]
        if parking_time > fees[0]:
            car_data[ck] += fees[3] * get_time(parking_time - fees[0], fees[2])

    car_data = list(car_data.items())
    car_data.sort()
    return list(map(list, zip(*car_data)))[1]


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]), [14600, 34400, 5000])
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]), [0, 591])
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]), [14841])
