"""
TapeEquilibrium
https://app.codility.com/programmers/lessons/3-time_complexity/
"""


def solution(A):
    answer = float('inf')
    a = sum(A[:1])
    b = sum(A[1:])
    answer = min(answer, abs(a - b))
    for p in range(len(A) - 1):
        answer = min(answer, abs(a - b))
        num = A[p + 1]
        a += num
        b -= num
    return answer


print(solution([3, 1, 2, 4, 3]))
print(solution([-100, 2]))
