def solution(n):
    count = 0

    # k는 연속된 숫자의 개수로 시작
    k = 1
    while (k * (k - 1)) // 2 < n:
        # 연속된 k개의 자연수의 합을 구성할 수 있는지를 확인
        if (n - (k * (k - 1)) // 2) % k == 0:
            count += 1
        k += 1

    return count

# 예시를 사용한 테스트
n = 15
print(solution(n))  # 4
