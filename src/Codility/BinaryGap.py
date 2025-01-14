"""
BinaryGap
https://app.codility.com/programmers/lessons/1-iterations/
"""


def solution(N):
    answer = 0
    index = 0
    data = format(N, f"0b")
    for i in range(1, len(data)):
        if data[i] == "1":
            answer = max(answer, i - index - 1)
            index = i

    return answer


print(solution(1))
print(solution(5))
print(solution(529))
print(solution(2147483647))
