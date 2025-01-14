import heapq


def solution(alp, cop, problems):
    inf = float('inf')
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]  # 문제를 안 풀고 1시간씩 능력을 키우는 방법도 있음.

    al_max, co_max = -inf, -inf
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        al_max = max(al_max, alp_req)
        co_max = max(co_max, cop_req)

    dist = [[inf for _ in range(151)] for _ in range(151)]
    dist[alp][cop] = 0

    q = [(0, alp, cop)]
    while q[0][1] < al_max or q[0][2] < co_max:
        ncost, nalp, ncop = heapq.heappop(q)

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:  # 매번 문제를 푸는 이유: 문제를 여러번 풀 수 있기 때문
            if nalp >= alp_req and ncop >= cop_req:  # 현재 능력으로 풀수 있는 문제
                new_al = min(150, nalp + alp_rwd)
                new_co = min(150, ncop + cop_rwd)
                new_cost = ncost + cost

                if dist[new_al][new_co] > new_cost:
                    dist[new_al][new_co] = new_cost
                    heapq.heappush(q, (new_cost, new_al, new_co))
    return q[0][0]