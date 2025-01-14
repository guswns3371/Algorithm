"""
PermCheck
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(A):
    dp = dict()
    for i in range(len(A)):
        if A[i] not in dp:
            dp[A[i]] = 1
        else:
            return 0

    if len(dp.keys()) < max(A):
        return 0

    return 1


print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3, 2, 10]))
print(solution([4, 1, 3, 2, 3, 5, 6]))
print(solution([4, 1, 3, 2, 5, 6]))
print(solution([4, 1, 3]))
