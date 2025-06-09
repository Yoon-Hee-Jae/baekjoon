def solution(topping):
    from collections import Counter
    
    total_counter = Counter(topping)
    left_toppings = set()
    right_toppings = len(total_counter)
    
    answer = 0 
    
    for i in range(len(topping)-1):
        left_toppings.add(topping[i])
        
        total_counter[topping[i]] -= 1
        if total_counter[topping[i]] == 0:
            right_toppings -= 1
        
        if len(left_toppings) == right_toppings:
            answer += 1 
            
    return answer