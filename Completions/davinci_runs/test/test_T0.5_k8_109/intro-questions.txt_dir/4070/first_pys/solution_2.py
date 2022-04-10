

def solution(n):
    answer = 0
    while n >= 10:
        answer += 1
        n = len(str(n))
    return answer