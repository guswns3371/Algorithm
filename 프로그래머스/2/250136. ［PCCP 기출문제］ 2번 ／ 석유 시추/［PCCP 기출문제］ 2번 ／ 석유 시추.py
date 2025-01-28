from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(land):
    def bfs(x, y, visited):
        visited[x][y] = 1
        history = [[x, y]]
        q = deque([[x, y]])

        while q:
            qx, qy = q.popleft()
            for i in range(4):
                xx = qx + dx[i]
                yy = qy + dy[i]
                if 0 <= xx < n and 0 <= yy < m:
                    if land[xx][yy] == 1 and visited[xx][yy] == 0:
                        history.append([xx, yy])
                        q.append([xx, yy])
                        visited[xx][yy] = 1
        return history

    n = len(land)
    m = len(land[0])
    oil_type = -1
    oil_val_map = {0: 0}

    # mark land
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(m):
        for x in range(n):
            if land[x][y] == 1 and visited[x][y] == 0:
                routes = bfs(x, y, visited)
                amount = len(routes)
                if oil_type not in oil_val_map:
                    oil_val_map[oil_type] = amount

                for rx, ry in routes:
                    land[rx][ry] = oil_type
                oil_type -= 1

    answer = 0
    for i in range(m):
        total_oil_type = set()
        for j in range(n):
            cur_oil_type = land[j][i]
            total_oil_type.add(cur_oil_type)
        answer = max(answer, sum(oil_val_map[t] for t in total_oil_type))

    return answer