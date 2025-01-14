check = ["RT", "CF", "JM", "AN"]


def solution(survey, choices):
    answer = ''
    mbti_map = dict(zip(*"RTCFJMAN".split(), [0] * 8))
    for i, sur in enumerate(survey):
        choice = choices[i] - 4
        left, right = sur
        if choice < 0:
            mbti_map[left] += abs(choice)
        elif choice > 0:
            mbti_map[right] += abs(choice)
    for cdata in check:
        a, b = cdata

        if mbti_map[a] >= mbti_map[b]:
            answer += a
        else:
            answer += b

    return answer
