

N = int(input())

odd = 0
for i in range(1, N+1):
    if i % 2 == 1:
        odd += 1

print(odd/N)
