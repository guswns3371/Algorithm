"""
LongestPassword
https://app.codility.com/programmers/trainings/1/
"""
import re


def solution(S):
    answer = -1
    for s in S.split():
        m = re.findall("[^a-zA-Z0-9]", s)
        if not m:
            letter_cnt = 0
            digit_cnt = 0
            for ss in s:
                if ss.isnumeric():
                    digit_cnt += 1
                elif ss.isalpha():
                    letter_cnt += 1
            if letter_cnt % 2 == 0 and digit_cnt % 2 == 1:
                answer = max(answer, len(s))

    return answer


print(solution('test 5 a0A pass007 ?xy1'))
