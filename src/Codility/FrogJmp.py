"""
FrogJmp
https://app.codility.com/programmers/lessons/3-time_complexity/
"""


def solution(X, Y, D):
    dist = Y - X
    if dist == 0:
        return 0
    data = dist / D
    if data > int(data):
        return int(data) + 1
    return int(data)


print(solution(10, 85, 30))
print(solution(10, 10, 30))
print(solution(10, 13, 1))
print(solution(10, 13, 1000))
