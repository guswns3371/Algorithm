"""
모음 사전
https://programmers.co.kr/learn/courses/30/lessons/84512
"""


def solution(word):
    answer = result.index(word)
    return answer


data = ["", "A", "E", "I", "O", "U"]
result = set()
for a in range(6):
    for b in range(6):
        for c in range(6):
            for d in range(6):
                for e in range(6):
                    temp = data[a] + data[b] + data[c] + data[d] + data[e]
                    result.add(temp)
result = sorted(result)

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
