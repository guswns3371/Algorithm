"""
MaxCounters
https://app.codility.com/programmers/lessons/4-counting_elements/
"""


def solution(N, A):
    data = dict()
    max_data = 0
    check = True
    for i in range(len(A)):
        if A[i] == N + 1:
            if check and data:
                max_data += max(data.values())
                data = dict()
                check = False
        else:
            if A[i] - 1 not in data:
                data[A[i] - 1] = 1
            else:
                data[A[i] - 1] += 1
            check = True

    answer = [0 for _ in range(N)]
    for i in range(N):
        if i not in data:
            answer[i] = max_data
        else:
            answer[i] = max_data + data[i]
    return answer


print(solution(5, [3, 4, 4, 6, 1, 4, 4, 6, 3, 4, 6, 2]))
print(solution(5, [6, 6, 6, 6, 6, 6]))
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
