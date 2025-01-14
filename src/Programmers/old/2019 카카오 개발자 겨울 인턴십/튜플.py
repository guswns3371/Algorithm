"""
튜플
https://programmers.co.kr/learn/courses/30/lessons/64065
"""


def solution(s):
    answer = []
    data = []
    temp = set()
    i = 1
    while i < len(s) - 1:
        if s[i] == "," and s[i + 1] == "{":
            i += 1
        elif s[i].isnumeric():
            start = i
            while s[i].isnumeric():
                i += 1
            temp.add(int(s[start:i]))
            continue
        elif s[i] == "}":
            data.append(temp)
            temp = set()
        i += 1
    data.sort(key=lambda x: len(x))

    for i in range(len(data)):
        if not answer:
            answer.append(list(data[i])[0])
        else:
            item = data[i] - set(answer)
            answer.append(list(item)[0])
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
