

# Solution 1
def solution(n):
    answer = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
        answer += 1
    return answer

# Solution 2
def solution(n):
    answer = 0
    while n > 1:
        n = n // 2 if n % 2 == 0 else n - 1
        answer += 1
    return answer
