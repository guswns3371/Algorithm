dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(min(n, m) // 2):
    for _ in range(r):

        peice = [n - 2 * i - 1, m - 2 * i - 1]

        xx = i
        yy = i
        old = arr[xx][yy]
        for k in range(4):
            prange = peice[k % 2]
            if k == 0:
                prange -= 1
            for _ in range(prange):
                xx += dx[k]
                yy += dy[k]
                now = arr[xx][yy]
                arr[xx][yy] = old
                old = now
            xx += dx[k]
            yy += dy[k]
            if k == 3:
                arr[xx][yy] = old
            xx -= dx[(k + 1) % 4]
            yy -= dy[(k + 1) % 4]
for a in arr:
    print(*a, sep=" ")