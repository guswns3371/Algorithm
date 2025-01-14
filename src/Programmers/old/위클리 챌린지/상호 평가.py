"""
2주차_상호 평가
https://programmers.co.kr/learn/courses/30/lessons/83201
"""


def solution(scores):
    answer = ''
    n = len(scores)
    # 리스트 행렬 뒤집기
    scores = [[i[j] for i in scores] for j in range(n)]
    scores = list(map(list, zip(*scores)))

    for i in range(n):
        i_score = scores[i]
        max_score = max(i_score)
        max_count = i_score.count(max_score)
        min_score = min(i_score)
        min_count = i_score.count(min_score)
        if (i_score[i] == max_score and max_count == 1) or (i_score[i] == min_score and min_count == 1):
            i_score.pop(i)
        mean = sum(i_score) / len(i_score)
        if mean >= 90:
            answer += "A"
        elif 80 <= mean < 90:
            answer += "B"
        elif 70 <= mean < 80:
            answer += "C"
        elif 50 <= mean < 70:
            answer += "D"
        elif mean < 50:
            answer += "F"

    return answer


print(solution(
    [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print(solution([[50, 90], [50, 87]]))
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
