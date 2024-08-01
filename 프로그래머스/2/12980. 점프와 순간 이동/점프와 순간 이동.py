def solution(N):
    battery_usage = 0
    
    while N > 0:
        if N % 2 == 0:
            N //= 2
        else:
            N -= 1
            battery_usage += 1
    
    return battery_usage