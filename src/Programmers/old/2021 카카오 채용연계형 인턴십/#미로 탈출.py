"""
미로 탈출
https://programmers.co.kr/learn/courses/30/lessons/81304
"""
from collections import deque
import heapq


def dprint(data):
    for i in range(len(data)):
        print(i, data[i])
    print()


def flip(a, b, data):
    data[a][b] *= -1
    data[b][a] *= -1


def bfs(data, n, start, end, traps):
    tmode = [0 for _ in range(n + 1)]
    dist = [float('inf') for _ in range(n + 1)]
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    q = []
    dist[start] = 0
    heapq.heappush(q, [0, start])

    while q:
        qcost, now = heapq.heappop(q)
        print(f"{now=}")
        if qcost > dist[now]:
            continue

        if now == end:
            return qcost

        if now in traps:
            tmode[now] = (tmode[now] + 1) % 2
            for k in range(2):
                for i in data[now][k]:
                    tmode[i[0]] = (tmode[i[0]] + 1) % 2

        print(f"{tmode=}")
        for i in data[now][tmode[now]]:
            near, cost = i
            if visited[now][near] == 0:
                if dist[near] > qcost + cost:
                    visited[now][near] = 1
                    dist[near] = qcost + cost
                    q.append([qcost + cost, near])


def solution(n, start, end, roads, traps):
    answer = 0
    data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for road in roads:
        a, b, c = road
        data[a][b] = c
        data[b][a] = -c

    dprint(data)
    # answer = bfs(data, n, start, end, traps)
    return answer


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
