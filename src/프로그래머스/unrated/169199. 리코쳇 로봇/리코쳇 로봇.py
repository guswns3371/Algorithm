from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(board):
    robot = None
    board = [list(x) for x in board]
    x_len = len(board)
    y_len = len(board[0])
    for x in range(x_len):
        for y in range(y_len):
            if board[x][y] == "R":
                robot = [x, y]
                board[x][y] = "."

    visited = [[False for _ in range(y_len)] for _ in range(x_len)]
    visited[robot[0]][robot[1]] = True
    q = deque([[0, robot[0], robot[1]]])
    while q:
        count, x, y = q.popleft()
        for k in range(4):
            xx = x
            yy = y

            while 0 <= xx < x_len and 0 <= yy < y_len and board[xx][yy] != "D":
                xx += dx[k]
                yy += dy[k]
            else:
                xx -= dx[k]
                yy -= dy[k]
                
            if 0 <= xx < x_len and 0 <= yy < y_len:
                if board[xx][yy] == "G":
                    return count + 1
                if not visited[xx][yy] and board[xx][yy] == ".":
                    visited[xx][yy] = True
                    q.append([count + 1, xx, yy])
    return -1