"""
CountDiv
https://app.codility.com/programmers/lessons/5-prefix_sums/
"""


def solution(A, B, K):
    count = 0
    n = A
    if n % K != 0:
        n += K - A % K
    if n <= B:
        count = (B // K) - (n // K) + 1
    return count


print(solution(6, 11, 2))
print(solution(0, 0, 1))
print(solution(11, 22, 3))
print(solution(10001, 299992, 3))
