"""
https://school.programmers.co.kr/learn/courses/30/lessons/140107
"""
import math


def solution(k, d):
    def get_x(y):
        return math.sqrt(d ** 2 - y ** 2)

    answer = 0
    for y in range(0, d + 1, k):
        x = get_x(y)
        answer += int(x // k) + 1  # 점 개수니까 +1
    return answer


print(solution(2, 4))
print(solution(1, 5))
