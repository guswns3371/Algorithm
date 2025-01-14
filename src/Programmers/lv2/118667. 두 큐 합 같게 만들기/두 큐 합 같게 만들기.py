def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) / 2
    current = sum(queue1)
    q = queue1 + queue2 + queue1

    answer = 0
    i = 0
    j = len(queue1) - 1
    while True:
        if current == target:
            return answer
        if current < target:
            j += 1
            if j >= len(q):
                return -1
            current += q[j]
        else:
            current -= q[i]
            i += 1
        answer += 1
