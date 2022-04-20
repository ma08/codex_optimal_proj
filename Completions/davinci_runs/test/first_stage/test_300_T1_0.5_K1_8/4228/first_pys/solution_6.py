

N, L = map(int, input().split())
sum = 0
for i in range(N):
    sum += L + i
min = sum
for i in range(N):
    if abs(sum - (L + i)) < min:
        min = abs(sum - (L + i))
print(sum - min)