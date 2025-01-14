"""
PermMissingElem
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
"""


def solution(A):
    set_a = set(A)
    data = set([i for i in range(1, len(A) + 2)])
    data -= set_a
    return list(data)[0]


print(solution([2, 3, 1, 5]))
print(solution([1]))
