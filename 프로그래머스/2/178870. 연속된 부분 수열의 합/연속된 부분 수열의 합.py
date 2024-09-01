def solution(sequence, k):
    start = 0
    end = 0
    current_sum = sequence[0]
    n = len(sequence)
    best_length = float('inf')
    result = [-1,-1]
    
    while start < n and end < n:
        if current_sum == k:
            if end - start < best_length:
                best_length = end - start
                result = [start,end]
                
            current_sum -= sequence[start]
            start += 1
            
        elif current_sum < k:
            end += 1
            if end < n:
                current_sum += sequence[end]
                
        else:
            current_sum -= sequence[start]
            start += 1
                
            
    return result