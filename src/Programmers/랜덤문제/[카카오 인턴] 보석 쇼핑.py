"""
[카카오 인턴] 보석 쇼핑
https://programmers.co.kr/learn/courses/30/lessons/67258
"""
from collections import defaultdict


def solution(gems):
    n = len(set(gems))
    lo = 0
    hi = 0
    answer = []
    while hi < len(gems):
        map_data = defaultdict(int)
        while hi < len(gems) and len(map_data.keys()) < n:
            map_data[gems[hi]] += 1
            hi += 1

        if len(map_data.keys()) < n:
            break

        while lo < hi:
            if map_data[gems[lo]] > 1:
                map_data[gems[lo]] -= 1
                lo += 1
            else:
                break

        answer.append([hi - lo - 1, lo + 1, hi])
        lo += 1
        hi = lo

    answer.sort()
    return answer[0][1:]


print(solution(["1", "1", "1", "2", "3", "1", "1", "1", "1", "2", "3", "1"]), [3, 5])
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]), [3, 7])
print(solution(["AA", "AB", "AC", "AA", "AC"]), [1, 3])
print(solution(["XYZ", "XYZ", "XYZ"]), [1, 1])
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]), [1, 5])
print(solution(["A", "A", "A", "B", "B"]), [3, 4])
print(solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]), [8, 10])
print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"]), [3, 7])
print(solution(["A"]), [1, 1])
