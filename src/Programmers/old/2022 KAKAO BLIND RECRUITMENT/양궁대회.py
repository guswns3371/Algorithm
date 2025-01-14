"""
양궁대회
https://programmers.co.kr/learn/courses/30/lessons/92342
ㄷㅂ 풀었다!!!
"""
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def solution(n, info):
    def get_gap(ryan_info):
        ryan_score = 0
        apeach_score = 0
        for i in range(11):
            if info[i] >= ryan_info[i]:
                if info[i] != 0:
                    apeach_score += 10 - i
            elif info[i] < ryan_info[i]:
                ryan_score += 10 - i

        if ryan_score > apeach_score:
            return True, abs(ryan_score - apeach_score)
        else:
            return False, abs(ryan_score - apeach_score)

    def dfs(data, total, score, check):

        if total == n:
            flag, gap = get_gap(data)
            if flag and data not in answer[gap]:
                answer[gap].append(data[:])
            return gap if flag else -float('inf')

        if tuple(data) in dp:
            return dp[tuple(data)]

        dtemp = -1
        for i in range(11):
            if check & (1 << (10 - i)) == 0:
                data[i] += 1
                temp = -1
                if info[i] < data[i]:  # 이긴 과녁은 더이상 고려하지 않도록 비트마스킹!
                    temp = max(temp, dfs(data, total + 1, score + 10 - i, check | (1 << (10 - i))))
                else:
                    temp = max(temp, dfs(data, total + 1, score, check))
                dp[tuple(data)] = temp
                data[i] -= 1

                dtemp = max(dtemp, temp)

        dp[tuple(data)] = dtemp
        return dp[tuple(data)]

    dp = dict()
    answer = defaultdict(list)
    dfs([0 for _ in range(11)], 0, 0, 0)

    if len(answer.keys()) > 0:
        max_gap = max(answer.keys())
        data = answer[max_gap]
        data.sort(key=lambda x: -sum([x[i] * (10 ** i) for i in range(11)]))
        return data[0]

    return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]), [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0])
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [-1])
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]), [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0])
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]), [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2])
