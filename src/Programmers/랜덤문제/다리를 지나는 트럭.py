"""
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0 for _ in range(bridge_length)])
    total_weight = 0
    while q:
        total_weight -= q.popleft()
        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

        time += 1
        print(q, truck_weights)
    return time


print(solution(2, 10, [7, 4, 5, 6]), 8)
print(solution(3, 10, [7, 4, 5, 3, 2, 1, 9]), 14)
print(solution(100, 100, [10]), 101)
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)
