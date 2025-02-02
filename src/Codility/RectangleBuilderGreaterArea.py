from collections import Counter


def solution(A, X):
    answer = 0

    # make available fence list
    available = []
    for k, v in Counter(A).items():
        if v >= 4:
            if k * k >= X:
                answer += 1
            available.append(k)
        elif v >= 2:
            available.append(k)
    available.sort()  # available 리스트에 두 개 만 고르면 직사각형이 만들어짐

    left = 0
    right = len(available) - 1
    while left < right:
        area = available[left] * available[right]
        if area >= X:
            answer += right - left  # right - left 값 자체가 경우의 수.
            right -= 1
        else:
            left += 1

        if answer > 10 ** 9:
            return -1

    return answer


print(solution([1], 10))
print(solution([x % 44_000 for x in range(1, 900_000)], 1))
print(solution([1, 2, 5, 1, 1, 2, 3, 5, 1], 5))
