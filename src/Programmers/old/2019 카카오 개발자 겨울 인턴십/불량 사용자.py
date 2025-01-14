"""
불량 사용자
https://programmers.co.kr/learn/courses/30/lessons/64064
"""
from itertools import product


def solution(user_id, banned_id):
    data = []
    result = set()
    for ban in banned_id:
        temp = []
        for user in user_id:
            if len(user) == len(ban):
                for i in range(len(ban)):
                    if not (ban[i] == "*" or ban[i] == user[i]):
                        break
                else:
                    temp.append(user)
        data.append(temp)

    for case in product(*data):
        if len(case) == len(set(case)):
            k = "_".join(sorted(list(case)))
            result.add(k)
    return len(result)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
