"""
호텔 방 배정
https://programmers.co.kr/learn/courses/30/lessons/64063
이진 탐색 ㄴㄴ -> union find ?
"""
import sys

sys.setrecursionlimit(10 ** 6)


def find_parent(num, rooms):
    if num not in rooms:
        rooms[num] = num + 1
        return num

    temp = find_parent(rooms[num], rooms)
    rooms[num] = temp + 1
    return temp


def solution(k, room_number):
    answer = []
    rooms = dict()

    for rnum in room_number:
        empty = find_parent(rnum, rooms)
        answer.append(empty)
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(11, [1, 9, 7, 1, 5, 1]))
