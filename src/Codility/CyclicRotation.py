"""
CyclicRotation
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
"""


def solution(A, K):
    if not A:
        return A
    K %= len(A)
    return A[-K:] + A[:-K]


print(solution([3, 8, 9, 7, 6], 3))
print(solution([3, 8, 9, 7, 6], 8))
print(solution([0, 0, 0], 1))
print(solution([1, 2, 3, 4], 4))
print(solution([i for i in range(100)], 201))
