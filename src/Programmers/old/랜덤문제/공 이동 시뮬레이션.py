"""
공 이동 시뮬레이션
https://programmers.co.kr/learn/courses/30/lessons/87391
아이디어 : https://prgms.tistory.com/108 공들을 한꺼번에 옮긴다
참고 : https://comdoc.tistory.com/488
이걸 어떻게 생각해..
"""
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 시간 초과
def solution1(n, m, x, y, queries):
    def move_all(i, d):
        move = dict()
        for bk, bv in balls.items():
            bx, by = bk
            xx = bx + dx[i] * d
            yy = by + dy[i] * d
            if not (0 <= xx < n and 0 <= yy < m):
                if xx < 0:
                    xx = 0
                elif xx >= n:
                    xx = n - 1
                if yy < 0:
                    yy = 0
                elif yy >= m:
                    yy = m - 1
            print(f"{(bx, by)} -> {(xx, yy)}")
            if (xx, yy) not in move:
                move[(xx, yy)] = 0
            move[(xx, yy)] += bv
        return move

    balls = dict([(i, j), 1] for j in range(m) for i in range(n))

    print(balls)
    for qi, qd in queries:
        print(f"{qi=} {(dx[qi], dy[qi])} {qd=}", balls)
        balls = move_all(qi, qd)

    return balls[(x, y)]


def solution(n, m, x, y, queries):
    top = bottom = x
    left = right = y
    for d, dx in queries[::-1]:
        if d == 0:
            if left != 0:
                left += dx
                if left > m - 1:
                    left = m - 1
            right += dx
            if right > m - 1:
                right = m - 1
        elif d == 1:
            left -= dx
            if left < 0:
                left = 0
            if right != m - 1:
                right -= dx
                if right < 0:
                    right = 0
        elif d == 2:
            if top != 0:
                top += dx
                if top > n - 1:
                    top = n - 1
            bottom += dx
            if bottom > n - 1:
                bottom = n - 1
        elif d == 3:
            top -= dx
            if top < 0:
                top = 0
            if bottom != n - 1:
                bottom -= dx
        if top > n - 1 or bottom < 0 or left > m - 1 or right < 0:
            return 0
    return (bottom - top + 1) * (right - left + 1)


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]), 4)
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]), 2)
