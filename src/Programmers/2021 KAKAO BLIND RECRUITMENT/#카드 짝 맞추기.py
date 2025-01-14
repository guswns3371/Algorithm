"""
카드 짝 맞추기 https://programmers.co.kr/learn/courses/30/lessons/72415
3 3 4 6
"""
from collections import defaultdict

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(board, r, c):
    answer = 0
    n = len(board)
    grim = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                grim[board[i][j]].append([i, j])
    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
