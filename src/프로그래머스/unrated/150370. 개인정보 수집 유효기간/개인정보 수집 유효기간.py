def solution(today, terms, privacies):
    answer = []
    today_count = convert(today)
    term_map = dict((x[0], float(x[2:])) for x in terms)
    for i, privacy in enumerate(privacies):
        when, term = privacy.split(" ")
        days = (today_count - convert(when)) / 28
        if days >= term_map[term]:
            answer.append(i + 1)
    answer.sort()
    return answer


def convert(s):
    s = s.split(".")
    return int(s[0]) * 12 * 28 + int(s[1]) * 28 + int(s[2])