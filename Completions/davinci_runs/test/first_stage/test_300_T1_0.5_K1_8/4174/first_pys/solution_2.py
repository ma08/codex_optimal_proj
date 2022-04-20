

N, X = map(int, input().split())
L = list(map(int, input().split()))

current = 0
count = 0
for i in range(N):
    current += L[i]
    if current <= X:
        count += 1
print(count)