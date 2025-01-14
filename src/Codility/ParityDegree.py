"""
ParityDegree
https://app.codility.com/programmers/trainings/5/parity_degree/
"""


def solution(N):
    k = 0
    while N % 2 == 0:
        N >>= 1
        k += 1
    return k


print(solution(24))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(888))
