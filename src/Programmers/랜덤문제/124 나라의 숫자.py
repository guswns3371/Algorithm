"""
124 나라의 숫자
https://programmers.co.kr/learn/courses/30/lessons/12899
참고 : https://minnnne.tistory.com/66

3으로 나눠지면 나머지를 4로 설정, 몫에 1을 뺌
"""


def solution(n):
    answer = ''

    while n:
        mok = n // 3
        rest = n % 3

        if rest == 0:
            answer = "4" + answer
            n = mok - 1
        else:
            answer = str(rest) + answer
            n = mok

    return answer


print(solution(1), 1)
print(solution(2), 2)
print(solution(3), 4)
print(solution(4), 11)
print(solution(15), 114)
print(solution(24), 214)
print(solution(27), 224)
