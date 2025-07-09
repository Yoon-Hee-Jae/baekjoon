def solution(my_string, is_prefix):
    for i in range(len(my_string) + 1):  # +1을 해줘야 전체 문자열도 포함됨
        if my_string[:i] == is_prefix:
            return 1
    return 0
