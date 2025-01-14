"""
복서 정렬하기
https://programmers.co.kr/learn/courses/30/lessons/85002
"""


def solution(weights, head2head):
    answer = []
    n = len(head2head)
    for i in range(n):
        win, lose, non, bigger = 0, 0, 0, 0
        for j in range(n):
            if i != j:
                if head2head[i][j] == "W":
                    win += 1
                    if weights[i] < weights[j]:
                        bigger += 1
                elif head2head[i][j] == "L":
                    lose += 1
                elif head2head[i][j] == "N":
                    non += 1
        if non == n - 1:
            win = 0
        elif lose > 0:
            win = win / (win + lose)
        else:
            win = 1
        answer.append([win, bigger, weights[i], i + 1])

    answer.sort(key=lambda x: (-x[0], -x[1], -x[2], x[0]))
    return list(list(zip(*answer))[-1])


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))
