

def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        answer += 1
    return answer

print(solution(11))
print(solution(14))
print(solution(61441))
print(solution(571576))
print(solution(2128506))