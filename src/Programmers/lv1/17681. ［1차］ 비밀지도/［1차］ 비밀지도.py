def solution(n, arr1, arr2):
    graph = []
    dmap = {"1": "#", "0": " "}
    for i in range(n):
        a1 = arr1[i]
        a2 = arr2[i]
        binary = bin(a1 | a2)[2:]
        binary = binary.rjust(n, "0")
        graph.append("".join(dmap[x] for x in binary))

    return graph
