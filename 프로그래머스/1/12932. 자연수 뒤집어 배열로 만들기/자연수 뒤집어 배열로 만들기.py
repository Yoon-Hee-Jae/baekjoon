def solution(n):
    answer = []
    a = str(n)
    for i in range(len(a)):
        value = int(a[i])
        answer.append(value)
    answer.reverse()
    return answer