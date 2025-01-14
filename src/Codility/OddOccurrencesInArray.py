"""
OddOccurrencesInArray
https://app.codility.com/programmers/lessons/2-arrays/
"""


def solution(A):
    data = dict()
    for a in A:
        if a not in data:
            data[a] = 1
        else:
            data[a] += 1
    for k, v in data.items():
        if v % 2 == 1:
            return k


print(solution([9, 3, 9, 3, 9, 7, 9]))
