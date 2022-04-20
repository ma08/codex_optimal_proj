
n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)

nice = []

for i in range(n):
    if a[i] == sum_a - a[i]:
        nice.append(i+1)

print(len(nice))
print(*nice)
