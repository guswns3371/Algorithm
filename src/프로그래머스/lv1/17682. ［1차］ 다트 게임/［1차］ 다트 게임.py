bonus = {"S":1,"D":2,"T":3}
opt = {"*":2, "#":-1}

def solution(dartResult):
    score = []
    c = 0
    start = 0
    snum = ""
    while c < len(dartResult):
        s = dartResult[c]
        if s.isnumeric():
            snum += s
        elif s in bonus.keys():
            score.append(int(snum))
            snum = ""
            score[-1] = score[-1] ** bonus[s]
        elif s == "*":
            for i in range(min(len(score), 2)):
                score[len(score) -1 - i] = score[len(score) -1 - i] * 2
        elif s == "#":
            score[-1] = -1 * score[-1]
            
        c += 1
    return sum(score)