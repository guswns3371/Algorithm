from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(land):
    def bfs(x, y, visited):
        visited[x][y] = 1
        sichu_locations = {y}
        amount = 1
        q = deque([[x, y]])

        while q:
            qx, qy = q.popleft()
            for i in range(4):
                xx = qx + dx[i]
                yy = qy + dy[i]
                if 0 <= xx < n and 0 <= yy < m:
                    if land[xx][yy] == 1 and visited[xx][yy] == 0:
                        q.append([xx, yy])
                        visited[xx][yy] = 1
                        amount += 1
                        sichu_locations.add(yy)

        for sichu_location in sichu_locations:
            oils[sichu_location] += amount

    n = len(land)
    m = len(land[0])
    oils = [0] * m

    visited = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(m):
        for x in range(n):
            if land[x][y] == 1 and visited[x][y] == 0:
                bfs(x, y, visited)

    return max(oils)
