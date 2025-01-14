"""
PassingCars
https://app.codility.com/programmers/lessons/5-prefix_sums/
"""


def solution(A):
    count = 0
    data = [0 for _ in range(len(A))]
    plist = []
    for i in range(len(A)):
        if A[i] == 0:
            plist.append(i)
            data[i] = data[i - 1]
        else:
            data[i] = data[i - 1] + 1

    n = data[-1]
    for p in plist:
        count += n - data[p]
    return -1 if count > 10 ** 9 else count



print(solution([0, 1, 0, 1, 1]))
print(solution([1]))
print(solution([0]))
print(solution([0, 1, 1, 0, 0, 0, 0, 1]))
print(solution([0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]))
