def solution(brown, yellow):
    total = brown + yellow  # 전체 격자의 수
    
    for h in range(1, int(total**0.5) + 1):
        if total % h == 0:  # h가 전체 격자의 약수인 경우
            w = total // h  # 가로 길이 w 계산
            if (w - 2) * (h - 2) == yellow:  # 노란색 격자의 조건을 만족하는지 확인
                return [w, h] 
    
    
