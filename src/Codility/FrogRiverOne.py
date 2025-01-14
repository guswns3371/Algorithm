"""
FrogRiverOne
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(X, A):
    count = 0
    dp = [0 for _ in range(X + 1)]
    for i in range(len(A)):
        if dp[A[i]] == 0:
            dp[A[i]] = 1
            count += 1
        if count == X:
            return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
print(solution(1, [1]))
print(solution(4, [1, 4, 1, 1, 2, 3, 3, 3, 3, 3]))
