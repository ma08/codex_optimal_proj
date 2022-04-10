

#-----main-----

a = list(map(int, input().split()))

b = [0] * 101

for x in a:
    b[x] += 1

result = 0

for i in range(len(b)):
    if b[i] > 1:
        result += 1

print(result)