

# My answer
n = int(input())
b = list(map(int, input().split()))

a = []
for i in range(n):
    if i == 0:
        a.append(b[i] - a[i+1])
    elif i == n-1:
        a.append(b[i-1] - a[i-1])
    else:
        a.append(max(b[i-1] - a[i-1], b[i] - a[i+1]))

print(sum(a))
