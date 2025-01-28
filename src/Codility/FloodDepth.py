def solution(A):
    # Implement your solution here
    mh = A[0]
    min_bh = 100000000

    answer = 0
    for i in range(1, len(A)):
        ch = A[i]
        bh = A[i - 1]
        
        if bh >= ch:
            min_bh = min(min_bh, ch)
            continue
        
        if ch < mh:
            answer = max(answer, ch - min_bh)
        elif ch >= mh:
            answer = max(answer, mh - min_bh)
            mh = ch
            min_bh = ch

    return answer