

A, B = map(int, input().split())

# A = 4
# B = 10

count = 0
while True:
    if A >= B:
        break
    A += 1
    count += 1

print(count)