from collections import Counter


def find_best_route(points, route):
    q = []
    time = 0

    for i in range(len(route) - 1):
        sx, sy = points[route[i] - 1]
        ex, ey = points[route[i + 1] - 1]
        # x 먼저 조절
        while sx != ex:
            q.append((sx, sy, time))
            if sx < ex:
                sx += 1
            else:
                sx -= 1
            time += 1

        # y 그 다음 조절
        while sy != ey:
            q.append((sx, sy, time))
            if sy < ey:
                sy += 1
            else:
                sy -= 1
            time += 1

    q.append((sx, sy, time))
    return q


def solution(points, routes):
    total = []
    for route in routes:
        total.extend(find_best_route(points, route))

    answer = 0
    for v in Counter(total).values():
        if v > 1:
            answer += 1
    return answer