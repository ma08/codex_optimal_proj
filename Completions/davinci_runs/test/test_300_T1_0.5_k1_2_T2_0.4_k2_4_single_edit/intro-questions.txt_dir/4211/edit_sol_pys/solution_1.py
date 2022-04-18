

n = int(input())
b = list(map(int, input().split()))

a = [0]

for i in range(n-1):
    if b[i+1] <= b[i+2]:
        a.append(b[i+2])
    else:
        a.append(b[i+1])

a.append(b[n-1])

print(sum(a))
