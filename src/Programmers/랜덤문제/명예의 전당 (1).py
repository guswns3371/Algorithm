"""
https://school.programmers.co.kr/learn/courses/30/lessons/138477
"""
import heapq


def solution(k, score):
    answer = []
    q = []
    for s in score:
        if len(q) < k:
            heapq.heappush(q, s)
        else:
            if q[0] < s:
                heapq.heappop(q)
                heapq.heappush(q, s)
        answer.append(q[0])

    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
