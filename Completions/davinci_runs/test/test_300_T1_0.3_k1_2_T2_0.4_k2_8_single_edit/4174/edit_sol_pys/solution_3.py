# abc 083 A

n, x = map(int, input().split())
l = list(map(int, input().split()))

# 初期値
count = 1
d = 0

for i in range(n):
    d += l[i]
    if d <= x:
        count += 1


# abc 083 B
n, a, b = map(int, input().split())

# 初期値
count = 0

for i in range(n+1):
    num = sum(list(map(int, list(str(i)))))
    if a <= num <= b:
        count += i

print(count)
print(count)
