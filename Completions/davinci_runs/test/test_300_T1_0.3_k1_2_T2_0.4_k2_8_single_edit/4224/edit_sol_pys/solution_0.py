

n = int(input())
a = list(map(int, input().split()))

count = 0

while True:
    for i in range(n):
        if a[i] % 2 == 1:
            break
    else:
        count += 1
        a = [x / 2 for x in a]
    else:
        break

print(count)
