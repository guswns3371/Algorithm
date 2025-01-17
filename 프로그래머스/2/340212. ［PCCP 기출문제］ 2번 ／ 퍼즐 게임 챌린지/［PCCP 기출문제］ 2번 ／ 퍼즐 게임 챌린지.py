def solution(diffs, times, limit):
    def check_level(level):
        total_t = 0
        for i in range(len(diffs)):
            d = diffs[i]
            t = times[i]
            
            if d <= level:
                total_t += t
            elif d > level:
                total_t += t + sum(times[i - 1:i + 1]) * (d - level)
            
            if total_t > limit:
                return False
        
        return total_t <= limit
    
    start = 1
    end = max(diffs)
    
    while start <= end:
        mid = (start + end) // 2
        check = check_level(mid)
        
        if check:
            end = mid - 1
        else:
            start = mid + 1
        
    
    return start