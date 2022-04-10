

def solution(n, a):
    sum = 0
    s = set()
    for i in range(n):
        sum += a[i]
        s.add(sum)
        if sum == 0:
            return n
    if sum % (n-1) == 0:
        return n-1
    return len(s)

n = int(input())
a = list(map(int, input().split()))
print(solution(n, a))