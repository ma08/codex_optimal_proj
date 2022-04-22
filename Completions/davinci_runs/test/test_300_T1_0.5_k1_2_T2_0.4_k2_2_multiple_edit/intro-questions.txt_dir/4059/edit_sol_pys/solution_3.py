
N = int(input())

result = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        c = N - a * b
        if c > 0: result += 1

print(ans)
