"""
도둑질 https://programmers.co.kr/learn/courses/30/lessons/42897
"""


def solution(money):
    answer = 0
    n = len(money)
    if n == 3:
        return
    dp = [[] for _ in range(n)]
    path = [[] for _ in range(n)]
    for i in range(n):
        if i == n - 1:
            path[i].append(0)
            path[0].append(i)
        else:
            path[i].append(i + 1)
            path[i + 1].append(i)

    for i in range(n):
        case = [x for x in list(set(range(n)) - {i}) if x not in path[i]]
        mcase = [money[i] for i in case]
        data = sorted(list(zip(mcase, case)))
        dp[i] += [data[-1][1]]
    print(dict(enumerate(dp)))
    return answer


print(solution([1, 2, 3, 1]))
print(solution([1, 2, 3]))
print(solution([1, 2, 3, 4, 5, 6]))
