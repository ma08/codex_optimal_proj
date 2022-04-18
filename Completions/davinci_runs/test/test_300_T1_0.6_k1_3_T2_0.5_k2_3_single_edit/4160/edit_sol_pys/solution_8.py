

n = int(input())
a = 100
count = 0

while a < n:
    a += a // 100
    count += 1

print(count)
