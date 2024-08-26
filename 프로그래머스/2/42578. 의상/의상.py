def solution(clothes):
    from collections import Counter
    from functools import reduce
    
    count = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), count.values(), 1) - 1
    return answer
