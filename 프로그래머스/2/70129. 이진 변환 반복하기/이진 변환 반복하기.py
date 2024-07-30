def solution(s):
    transform_count = 0
    removed_zeros = 0
    
    while s != "1":
        # 현재 문자열에서 0의 개수를 세고 제거합니다.
        zero_count = s.count('0')
        removed_zeros += zero_count
        s = s.replace('0', '')
        
        # 남은 문자열의 길이를 2진법으로 변환합니다.
        length = len(s)
        s = bin(length)[2:]  # bin() 함수는 '0b' 접두사를 붙이므로 이를 제거합니다.
        
        # 변환 횟수를 증가시킵니다.
        transform_count += 1
    
    return [transform_count, removed_zeros]

# 예시를 사용한 테스트
s = "0111010"
print(solution(s))  # [3, 5]
