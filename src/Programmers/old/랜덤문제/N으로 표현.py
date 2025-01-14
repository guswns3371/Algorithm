"""
N으로 표현
https://programmers.co.kr/learn/courses/30/lessons/42895
"""


def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        case = set()
        # N, NN, NNN ...
        case.add(int(str(N) * i))

        for j in range(0, i - 1):
            for op1 in dp[j]:
                for op2 in dp[i - j - 2]:
                    # i개의 N으로 만들 수 있는 숫자들을 case에 담는다.
                    if op1 - op2 >= 0:
                        case.add(op1 - op2)
                    case.add(op1 + op2)
                    case.add(op1 * op2)
                    if op2 != 0:
                        case.add(op1 // op2)
        if number in case:
            # i개의 N으로 만든 수들 중 number가 있을 경우
            answer = i
            break
        dp.append(case)
    return answer


print(solution(5, 12))
print(solution(2, 11))
