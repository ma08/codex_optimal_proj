
n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n-1):
    a.append(min(b[i], b[i+1]))

a.append(b[n-2])

print(sum(a))
