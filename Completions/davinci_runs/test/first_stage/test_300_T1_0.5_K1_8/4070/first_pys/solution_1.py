

def solution(n):
    answer = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            answer += 1
        i += 1
    return answer

print(solution(11))
print(solution(14))
print(solution(61441))
print(solution(571576))
print(solution(2128506))