

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

result = 0
for i in range(n):
    result += b[a[i] - 1]
    if i > 0 and a[i] == a[i - 1] + 1:
        result += c[a[i - 1] - 1]
print(result)
