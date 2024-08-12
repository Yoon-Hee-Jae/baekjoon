def solution(k, tangerine):
    # 귤의 크기별로 개수를 세기
    size_count = {}
    for size in tangerine:
        if size in size_count:
            size_count[size] += 1
        else:
            size_count[size] = 1
    
    # 귤 크기별 개수를 내림차순으로 정렬
    sorted_sizes = sorted(size_count.values(), reverse=True)
    
    # 귤 종류의 수를 최소화하기 위해 가장 많이 있는 것부터 채워나가기
    count = 0
    for amount in sorted_sizes:
        k -= amount
        count += 1
        if k <= 0:
            break
            
    return count
