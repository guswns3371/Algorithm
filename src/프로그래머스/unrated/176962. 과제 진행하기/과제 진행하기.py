from collections import deque


def solution(plans):
    def convert_time(s):
        s = s.split(":")
        return int(s[0]) * 60 + int(s[1])

    answer = []
    buff = deque([])
    data = [-1 for _ in range(1540)]

    plans.sort(key=lambda x: x[1])
    plans = [[x[0], convert_time(x[1]), int(x[2])] for x in plans]
    plans += [["", plans[-1][1] + plans[-1][2], 0]]

    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        name2, start2, playtime2 = plans[i + 1]
        for j in range(start, min(start2, start + playtime)):
            data[j] = i

    old = 0
    for i in range(plans[0][1], plans[-1][1] + 1):
        pi = data[i]
        if pi == -1:
            if buff:
                buff[-1][2] -= 1
                if buff[-1][2] == 0:
                    answer.append(buff[-1][0])
                    buff.pop()
        else:
            if pi != old and plans[old][2] > 0:
                buff.append(plans[old])
            plans[pi][2] -= 1
            if plans[pi][2] == 0:
                answer.append(plans[pi][0])
        old = pi

    while buff:
        name, start, playtime = buff.pop()
        answer.append(name)
    return answer