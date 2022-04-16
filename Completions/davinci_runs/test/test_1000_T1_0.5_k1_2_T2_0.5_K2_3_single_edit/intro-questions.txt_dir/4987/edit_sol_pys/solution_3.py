

# SOLUTION 1

n, k = map(int, input().split())

def solution(n, k):
    if n == 1:
        return k
    if k == 1:
        return 1
    return solution(n - 1, k) + solution(n, k - 1)

print(solution(n, k))
