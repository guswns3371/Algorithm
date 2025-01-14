"""
징검다리 https://programmers.co.kr/learn/courses/30/lessons/43236
"""


def fn(param):
    mid, rocks, n = param


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks = [0] + rocks + [distance]

    dist = [rocks[i + 1] - rocks[i] for i in range(6)]
    lo = min(dist) - 1
    hi = max(dist) + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        temp = fn((mid, rocks, n))

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
