
def solution(n, k):
    if n % 2 == 0:
        return "yes"
    return "no"

n, k = map(int, input().split())
print(solution(n, k))
