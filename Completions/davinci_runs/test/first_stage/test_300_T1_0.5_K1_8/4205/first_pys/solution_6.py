

n = int(input())
p = list(map(int, input().split()))

def check():
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] > p[j]:
                return "YES"
    return "NO"

print(check())