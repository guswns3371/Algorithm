"""
MissingInteger
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    data = dict()
    max_data = 0
    for a in set(A):
        if a not in data:
            data[a] = 1
            max_data = max(max_data, a)
        else:
            data[a] = 1
    for i in range(1, max_data + 1):
        if i not in data:
            return i
    return max_data + 1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
print(solution([-1000]))
print(solution([1000]))
print(solution([1, 2, 3, 4, 34, 234, 235, 2351, 213, 213]))
