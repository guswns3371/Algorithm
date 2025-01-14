"""
4주차_직업군 추천하기
https://programmers.co.kr/learn/courses/30/lessons/84325
"""
from collections import defaultdict


def solution(table, languages, preference):
    n = len(languages)
    result = defaultdict(int)
    for i in range(n):
        lang = languages[i]
        pref = preference[i]
        for lk, lv in data[lang].items():
            for val in lv:
                result[val] += lk * pref
    result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    return result[0][0]


data = defaultdict(dict)
temp = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"]
for t in temp:
    t = t.split(" ")
    category = t[0]
    for i, v in enumerate(t[1:]):
        if 5 - i not in data[v]:
            data[v][5 - i] = [category]
        else:
            data[v][5 - i].append(category)
for k in data.keys():
    data[k] = dict(sorted(data[k].items(), key=lambda x: -x[0]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
