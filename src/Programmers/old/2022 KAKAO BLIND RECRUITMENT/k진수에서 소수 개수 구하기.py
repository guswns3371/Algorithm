"""
k진수에서 소수 개수 구하기
https://programmers.co.kr/learn/courses/30/lessons/92335
"""
import math


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def convert(num, base):
    result = ""
    while num:
        result += str(num % base)
        num = num // base
    return result[::-1]


def solution(n, k):
    answer = 0
    knum = convert(n, k).split("0")
    for kn in knum:
        if kn and is_prime(int(kn)):
            answer += 1
    return answer


print(solution(437674, 3), 3)
print(solution(110011, 10), 2)
print(solution(3, 2), 1)
