import heapq

inf = float('inf')


def solution(n, paths, gates, summits):
    def get_intensity():
        q = []
        # 다익스트라 -> 가중치가 intensity
        intensity_dist = [inf for _ in range(n + 1)]

        # 우선순위 큐에 모든 gate를 넣는다 -> 모든 gate를 고려한 min intensity를 한번에 구할 수 있다.
        for gate in gates:
            intensity_dist[gate] = 0
            heapq.heappush(q, (0, gate))

        while q:
            intensity, now = heapq.heappop(q)
            if intensity_dist[now] < intensity or now in summits:
                continue

            for next_node, cost in graph[now]:
                new_intensity = max(cost, intensity)
                if intensity_dist[next_node] > new_intensity:
                    intensity_dist[next_node] = new_intensity
                    heapq.heappush(q, (new_intensity, next_node))

        answer = [0, inf]
        for summit in summits:
            if intensity_dist[summit] < answer[1]:
                answer = [summit, intensity_dist[summit]]

        return answer

    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    summits = list(set(summits))  # 상봉우리의 번호가 낮을 수록 우선순위가 높기 때문에 오름차순 정렬
    summits.sort()
    return get_intensity()