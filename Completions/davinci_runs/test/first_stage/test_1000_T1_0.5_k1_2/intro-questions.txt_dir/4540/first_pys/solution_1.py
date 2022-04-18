

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    print(sum(abs(a[j] - a[i]) for j in range(n) if j != i))