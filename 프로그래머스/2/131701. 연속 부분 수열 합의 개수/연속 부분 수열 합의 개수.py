def solution(elements):
    n = len(elements)
    elements_extended = elements * 2  # 원형 수열을 위해 두 배로 확장
    sum_set = set()  # 중복을 방지하기 위한 집합
    
    for i in range(n):
        current_sum = 0
        for j in range(1, n + 1):
            current_sum += elements_extended[i + j - 1]
            sum_set.add(current_sum)
    
    return len(sum_set)
