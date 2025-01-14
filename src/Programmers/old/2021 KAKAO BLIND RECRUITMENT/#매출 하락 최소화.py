"""
매출 하락 최소화 https://programmers.co.kr/learn/courses/30/lessons/72416
"""
from collections import deque


def lprint(data):
    for d in data:
        print(d)


def get_team(n, sales, indegree, path):
    temp, team, leaf, parent = [], [], [], []
    for i in range(n + 1):
        if indegree[i] == 0:
            temp.append(i)

    q = deque(temp)
    while q:
        now = q.popleft()
        temp = []
        for node in path[now]:
            indegree[node] -= 1
            temp.append((sales[node - 1], node))
            if indegree[node] == 0:
                q.append(node)
        if temp:
            team.append(sorted([(sales[now - 1], now)] + temp))
            parent.append(now)
        else:
            leaf.append(now)

    return team, leaf[1:], parent


def solution(sales, links):
    print()
    answer = float('inf')
    n = len(sales)
    indegree = [0 for _ in range(n + 1)]
    path = [[] for _ in range(n + 1)]

    for link in links:
        a, b = link
        indegree[b] += 1
        path[a].append(b)

    teams, leaf, parent = get_team(n, sales, indegree, path)
    employees = sorted([(sales[i], i + 1) for i in range(n)])

    lprint(teams)
    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
               [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(solution([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]))
