

n = int(input())

sum = 0

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        sum += i

print(sum)
