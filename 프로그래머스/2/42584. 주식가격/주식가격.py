def solution(prices):
    # 결과를 저장할 배열. 각 초에 대한 가격이 유지된 시간을 기록함.
    answer = [0] * len(prices)
    
    # 스택을 사용하여 인덱스를 저장
    stack = []
    
    for i in range(len(prices)):
        # 스택에 있는 인덱스의 가격보다 현재 가격이 낮으면 스택에서 제거하고 유지된 기간 계산
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        
        # 현재 인덱스를 스택에 추가
        stack.append(i)
    
    # 스택에 남은 인덱스들은 가격이 끝까지 떨어지지 않은 경우이므로 처리
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - 1 - idx
    
    return answer
