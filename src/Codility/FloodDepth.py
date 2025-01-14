"""
FloodDepth
https://app.codility.com/programmers/trainings/1/flood_depth/
참고 : https://codesays.com/2016/solution-to-flood-depth-by-codility/
"""


# 85%
def solution1(A):
    n = len(A)
    waters = [0 for _ in range(n)]
    if n == 1:
        return 0
    old_grad = A[1] - A[0]
    for i in range(2, n):
        grad = A[i] - A[i - 1]
        if old_grad <= 0 < grad or grad > 0:
            end = i
            start = -1
            min_val = -1
            for j in range(end - 1, -1, -1):
                if A[j] >= min_val:
                    start = j
                    min_val = A[j]
                    if min_val >= A[end]:
                        break
            if min_val < A[end]:
                for j in range(start + 1, end):
                    waters[j] = min_val - A[j]
            else:
                for j in range(start + 1, end):
                    waters[j] = A[end] - A[j]
        old_grad = grad

    return max(waters)


# 미친새끼
def solution(A):
    maxH = 0
    minH = 0
    maxD = 0
    d = 0
    for i, a in enumerate(A):
        if a > maxH:
            d = maxH - minH
            maxH = a
            minH = a
        elif a < minH:
            minH = a
        elif minH <= a <= maxH:
            d = a - minH
        maxD = max(maxD, d)
        print(f"{i=} {a=} {maxH=} {minH=} {maxD=} {d=}")
    return maxD


print(solution([1]))
print(solution([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]))
print(solution([1, 2, 3, 1, 2, 1, 5, 3, 3, 4, 2]))
print(solution([5, 8]))
print(solution([4, 3, 2, 3, 5]))
print(solution([2, 1, 3]))
print(solution([10 ** 9, 1, 10 ** 9]))
print(solution([10 ** 9 for _ in range(10)]))
print(solution([100000000, 1, 2, 99999999, 100000000, 1, 2, 99999999]))
