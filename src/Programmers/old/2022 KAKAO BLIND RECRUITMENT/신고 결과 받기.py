"""
신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/92334
"""


def solution(id_list, report, k):
    answer = []
    data = dict(zip(id_list, [0 for _ in range(len(id_list))]))
    rdata = dict()

    for r in report:
        uid, rid = r.split()
        if uid not in rdata:
            rdata[uid] = set()
        rdata[uid].add(rid)

    for rk, rv in rdata.items():
        for rvv in rv:
            data[rvv] += 1

    for dk, dv in data.items():
        count = 0
        if dk in rdata:
            for vv in rdata[dk]:
                if data[vv] >= k:
                    count += 1
        answer.append(count)
    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2), [2, 1, 1, 0])
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3), [0, 0])
