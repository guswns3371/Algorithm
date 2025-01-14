"""
ParkingBill
https://app.codility.com/programmers/trainings/5/parking_bill/
"""


def encode(data):
    t = data.split(":")
    return int(t[0]) * 60 + int(t[1])


def solution(E, L):
    start = encode(E)
    end = encode(L)
    if start == end:
        return 2
    if end - start < 60:
        return 5
    start += 60
    gap = end - start
    count = gap / 60
    count = int(count) + 1 if count > int(count) else int(count)
    return 5 + 4 * count


print(solution('10:00', '13:21'))
print(solution('09:42', '11:42'))
print(solution('09:42', '10:42'))
print(solution('09:42', '09:42'))
