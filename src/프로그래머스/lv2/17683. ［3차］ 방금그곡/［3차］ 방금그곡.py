def solution(m, musicinfos):
    answer = []
    for i, info in enumerate(musicinfos):
        start, end, title, data = info.split(",")
        term = convert(end) - convert(start)
        
        m = modify(m)
        data = modify(data)
        
        if term >= len(data):
            rep = term // len(data)
            data = data * rep + data[:term%len(data)]
        else:
            data = data[:term]
        
        if m in data:
            answer.append([-len(data), i, title])
            
    if not answer:
        return "(None)"
    
    answer.sort()
    return answer[0][-1]

def convert(t):
    t = t.split(":")
    return int(t[1]) + int(t[0]) * 60

lower_data = {
    "C#":"c",
    "D#":"d",
    "F#":"f",
    "G#":"g",
    "A#":"a",
             }
def modify(s):
    for k, v in lower_data.items():
        s = s.replace(k, v)
    return s
    