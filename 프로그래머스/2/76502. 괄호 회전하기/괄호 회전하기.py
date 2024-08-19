def is_valid(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in matching.values():  # 여는 괄호
            stack.append(char)
        elif char in matching.keys():  # 닫는 괄호
            if stack == [] or stack.pop() != matching[char]:
                return False
    
    return stack == []

def solution(s):
    n = len(s)
    valid_count = 0
    
    for i in range(n):
        rotated_s = s[i:] + s[:i]
        if is_valid(rotated_s):
            valid_count += 1
    
    return valid_count




