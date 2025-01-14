"""
3주차_퍼즐 조각 채우기
https://programmers.co.kr/learn/courses/30/lessons/84021
3배 -> 테스트 케이스 시간초과 : 11,13
1배 -> 테스트 케이스 실패 : 10
"""

from collections import deque


def get_piece(table, tn):
    data = []
    visited = [[0 for _ in range(tn)] for _ in range(tn)]

    for i in range(tn):
        for j in range(tn):
            if visited[i][j] == 0 and table[i][j] == 1:
                temp = [[i, j]]
                visited[i][j] = 1
                q = deque([[i, j]])
                while q:
                    a, b = q.popleft()
                    for k in range(4):
                        x = a + dx[k]
                        y = b + dy[k]
                        if 0 <= x < tn and 0 <= y < tn:
                            if visited[x][y] == 0 and table[x][y] == 1:
                                visited[x][y] = 1
                                q.append([x, y])
                                temp.append([x, y])
                data.append(temp)
    return data


def get_rect_piece(data):
    print(data)
    print(list(zip(*data)))
    dxs, dys = zip(*data)
    maxx, minx = max(dxs), min(dxs)
    maxy, miny = max(dys), min(dys)

    dn = max(abs(maxx - minx), abs(maxy - miny)) + 1
    rect = [[0 for _ in range(dn)] for _ in range(dn)]

    for d in data:
        rect[d[0] - minx][d[1] - miny] = 1
    return rect, dn


def check(x, y, game_board, piece, gn, pn):
    for px in range(pn):
        for py in range(pn):
            gx, gy = x + px, y + py
            if gn <= gx < 2 * gn and gn <= gy < 2 * gn:
                if piece[px][py] == 1:
                    if game_board[gx][gy] == 1:
                        for r in range(4):
                            xx = gx + dx[r]
                            yy = gy + dy[r]
                            if gn <= xx < 2 * gn and gn <= yy < 2 * gn:
                                if game_board[xx][yy] != 1:
                                    return False
                    else:
                        return False
            else:
                if piece[px][py] == 1:
                    return False
    return True


def three_times(data, n):
    result = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    for x in range(n, 2 * n):
        for y in range(n, 2 * n):
            result[x][y] += data[x - n][y - n]
    return result


def solution(game_board, table):
    answer = 0
    gn = len(game_board)
    game_board = three_times(game_board, gn)
    pieces = get_piece(table, gn)

    for piece in pieces:
        flag = False
        rpiece, pn = get_rect_piece(piece)

        for x in range(gn - pn + 1, 2 * gn + pn - 1):
            for y in range(gn - pn + 1, 2 * gn + pn - 1):

                for _ in range(4):
                    # 퍼즐 끼우기
                    for px in range(pn):
                        for py in range(pn):
                            gx, gy = x + px, y + py
                            if gn <= gx < 2 * gn and gn <= gy < 2 * gn:
                                game_board[gx][gy] += rpiece[px][py]
                    # 체크
                    if check(x, y, game_board, rpiece, gn, pn):
                        answer += len(piece)
                        flag = True
                    else:
                        # 퍼즐 빼기
                        for px in range(pn):
                            for py in range(pn):
                                gx, gy = x + px, y + py
                                if gn <= gx < 2 * gn and gn <= gy < 2 * gn:
                                    game_board[gx][gy] -= rpiece[px][py]
                    if flag:
                        # 퍼즐 맞음
                        break
                    else:
                        # 퍼즐 회전
                        rpiece = list(zip(*rpiece[::-1]))
                if flag:
                    break
            if flag:
                break
    return answer


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
print(solution(
    [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
     [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
     [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
     [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
    [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
     [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
     [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],
     [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]))

"""
# 1배 -> 테스트 케이스 실패 : 10
from collections import deque


def get_piece(table):
    data = []
    tn = len(table)
    visited = [[0 for _ in range(tn)] for _ in range(tn)]

    for i in range(tn):
        for j in range(tn):
            if visited[i][j] == 0 and table[i][j] == 1:
                temp = [[i, j]]
                visited[i][j] = 1
                q = deque([[i, j]])
                while q:
                    a, b = q.popleft()
                    for k in range(4):
                        x = a + dx[k]
                        y = b + dy[k]
                        if 0 <= x < tn and 0 <= y < tn:
                            if visited[x][y] == 0 and table[x][y] == 1:
                                visited[x][y] = 1
                                q.append([x, y])
                                temp.append([x, y])
                data.append(temp)
    return data


def get_rect_piece(data):
    dxs, dys = zip(*data)
    maxx, minx = max(dxs), min(dxs)
    maxy, miny = max(dys), min(dys)

    dn = max(abs(maxx - minx), abs(maxy - miny)) + 1
    rect = [[0 for _ in range(dn)] for _ in range(dn)]

    for d in data:
        rect[d[0] - minx][d[1] - miny] = 1
    return rect, dn


def check(x, y, game_board, piece, gn, pn):
    for i in range(pn):
        for j in range(pn):
            bx, by = x + i, y + j
            if piece[i][j] == 1:
                if game_board[bx][by] == 1:
                    for k in range(4):
                        xx = bx + dx[k]
                        yy = by + dy[k]
                        if 0 <= xx < gn and 0 <= yy < gn:
                            if game_board[xx][yy] != 1:
                                return False
                else:
                    return False

    return True


def solution(game_board, table):
    answer = 0
    gn = len(game_board)
    pieces = get_piece(table)

    for piece in pieces:
        flag = False
        rpiece, pn = get_rect_piece(piece)

        for x in range(gn - pn + 1):
            for y in range(gn - pn + 1):

                for _ in range(4):
                    # 퍼즐 끼우기
                    for px in range(pn):
                        for py in range(pn):
                            game_board[px + x][py + y] += rpiece[px][py]
                    # 체크
                    if check(x, y, game_board, rpiece, gn, pn):
                        answer += len(piece)
                        flag = True
                    else:
                        # 퍼즐 빼기
                        for px in range(pn):
                            for py in range(pn):
                                game_board[px + x][py + y] -= rpiece[px][py]
                    if flag:
                        # 퍼즐 맞음
                        break
                    else:
                        # 퍼즐 회전
                        rpiece = list(zip(*rpiece[::-1]))
                if flag:
                    break
            if flag:
                break

    return answer


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
"""