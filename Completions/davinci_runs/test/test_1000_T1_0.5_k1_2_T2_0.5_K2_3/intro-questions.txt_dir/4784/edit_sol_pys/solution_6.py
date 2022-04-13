
x = int(input())
n = int(input())

res = x
for i in range(n):
    res -= int(input())
    res -= int(input())

print(res)
