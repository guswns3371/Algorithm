"""
MinAvgTwoSlice
https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/
참고:https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=alwlren_00&logNo=221603639510
수학적 지식없이 못 푸는 문제
"""


def solution(A):
    min_val = sum(A[0:2]) / 2
    result = 0

    for i in range(3, len(A) + 1):
        avg = sum(A[i - 2:i]) / 2
        if min_val > avg:
            min_val = avg
            result = i - 2
        avg = sum(A[i - 3:i]) / 3
        if min_val > avg:
            min_val = avg
            result = i - 3
    return result


print(solution([4, 2, 2, 5, 1, 5, 8]))
print(solution([9, 1, 1, 1]))
