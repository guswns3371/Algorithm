"""
입실 퇴실
https://programmers.co.kr/learn/courses/30/lessons/86048

from copy import deepcopy
from itertools import combinations


def dfs(i, j, enter, leave, room, history, answer):
    if j >= len(leave):
        answer.append(history)
        return history

    if i < len(enter):
        room.append(enter[i])
        history.append(room)
        i += 1
        dfs(i, j, enter, leave, room, deepcopy(history), answer)
        i -= 1
        history.remove(room)
        room.remove(enter[i])

    if leave[j] in room:
        room.remove(leave[j])
        history.append(room)
        j += 1
        dfs(i, j, enter, leave, room, deepcopy(history), answer)
        j -= 1
        history.remove(room)
        room.append(leave[j])


def solution(enter, leave):
    answer = []
    data = [0 for _ in range(len(enter))]
    dfs(1, 0, enter, leave, [enter[0]], [[enter[0]]], answer)

    temp = set()
    for ans in answer:
        atemp = set()
        for room in ans:
            if len(room) > 1:
                for case in combinations(room, 2):
                    atemp.add(case)
        if not temp:
            temp = temp | atemp
        else:
            temp = temp & atemp

    for t in temp:
        data[t[0] - 1] += 1
        data[t[1] - 1] += 1
    return data
"""


def solution(enter, leave):
    n = len(enter)
    i, j = 0, 0
    room = set()
    answer = [0 for _ in range(n)]
    while j < n:
        if leave[j] in room:
            room.remove(leave[j])
            j += 1
            continue
        if enter[i] not in room:
            for one in room:
                answer[one - 1] += 1
            answer[enter[i] - 1] = len(room)
            room.add(enter[i])
            i += 1
    return answer


print(solution([1, 3, 2], [1, 2, 3]))
print(solution([1, 4, 2, 3], [2, 1, 3, 4]))
print(solution([3, 2, 1], [2, 1, 3]))
print(solution([3, 2, 1], [1, 3, 2]))
print(solution([1, 4, 2, 3], [2, 1, 4, 3]))
