

def solution(n):
    return n - sum(map(int, str(n)))

print(solution(11))