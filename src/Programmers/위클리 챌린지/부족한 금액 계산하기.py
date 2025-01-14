"""
1주차_부족한 금액 계산하기
https://programmers.co.kr/learn/courses/30/lessons/82612
"""


def solution(price, money, count):
    total_count = sum([i for i in range(1, count + 1)])
    answer = price * total_count - money
    return answer if answer > 0 else 0


print(solution(3, 20, 4))
