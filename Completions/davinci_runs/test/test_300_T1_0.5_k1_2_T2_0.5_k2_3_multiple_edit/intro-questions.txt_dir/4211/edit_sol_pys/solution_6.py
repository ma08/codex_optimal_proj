
n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n-1):
    if b[i] <= b[i+1]:
        a.append(b[i])
    else:
        a.append(b[i+1])

a.append(b[n-1])

print(sum(a))

# test
