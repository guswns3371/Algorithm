"""
타겟 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
"""


def dfs(numbers, target, index, value):
    if index >= len(numbers):
        if value == target:
            return 1
        return 0

    count = 0
    for i in [1, -1]:
        count += dfs(numbers, target, index + 1, value + i * numbers[index])
    return count


def solution(numbers, target):
    return dfs(numbers, target, 0, 0)


print(solution([1, 1, 1, 1, 1], 3))
