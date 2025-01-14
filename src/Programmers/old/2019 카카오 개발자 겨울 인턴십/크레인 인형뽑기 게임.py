"""
크레인 인형뽑기 게임
https://programmers.co.kr/learn/courses/30/lessons/64061
"""
from collections import deque


def solution(board, moves):
    answer = 0
    data = [deque([i for i in x if i != 0]) for x in list(map(list, zip(*board)))]
    bowl = deque([])

    for move in moves:
        dtmp = data[move - 1]
        if dtmp:
            item = dtmp.popleft()
            if bowl and item == bowl[-1]:
                bowl.pop()
                answer += 2
            else:
                bowl.append(item)
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
