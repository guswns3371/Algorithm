"""
https://school.programmers.co.kr/learn/courses/30/lessons/140108
"""

from collections import deque


def solution(s):
    x = s[0]
    answer = 0
    a, b = 0, 0
    q = deque(s)
    while q:
        e = q.popleft()
        if a == b:
            answer += 1
            a, b = 0, 0
            x = e
        if e == x:
            a += 1
        else:
            b += 1
    return answer


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
