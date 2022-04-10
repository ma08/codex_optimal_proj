K = int(input())

for num in range(7, 1000000, 10):
    if num % K == 0:
        print(num // 10)
        exit()

print(-1)
