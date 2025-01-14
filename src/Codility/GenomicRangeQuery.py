"""
GenomicRangeQuery
https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/
"""


def solution(S, P, Q):
    answer = []
    genome = dict({'A': 1, 'C': 2, 'G': 3, 'T': 4})
    data = []
    temp = [0 for _ in range(4)]
    for i in range(len(S)):
        temp[genome[S[i]] - 1] += 1
        data.append(temp.copy())

    for i in range(len(P)):
        p = P[i]
        q = Q[i]
        if p == q:
            answer.append(genome[S[p]])
        else:
            temp = [0 for _ in range(4)]
            for j in range(4):
                temp[j] = data[q][j] - data[p][j]
            temp[genome[S[p]] - 1] += 1
            for j in range(4):
                if temp[j] != 0:
                    answer.append(j + 1)
                    break

    return answer


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
print(solution("C", [0], [0]))
print(solution('AC', [0, 0, 1], [0, 1, 1]))
print(solution('TC', [0, 0, 1], [0, 1, 1]))
