"""
징검다리 건너기
https://programmers.co.kr/learn/courses/30/lessons/64062
참고 :
https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level3-%EC%A7%95%EA%B2%80%EB%8B%A4
%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0-Python

이분탐색 -> 미리 답이 정해져있다고 간주하여 푸는 방식
즉, mid값이 답이라고 정해둔 뒤, 이후에 답(mid) 검증
"""


def solution(stones, k):
    lo = 1
    hi = max(stones)
    while lo < hi:
        mid = (lo + hi) // 2

        gap = 0
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                gap += 1
            else:
                gap = 0
            if gap >= k:
                break

        if gap >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
