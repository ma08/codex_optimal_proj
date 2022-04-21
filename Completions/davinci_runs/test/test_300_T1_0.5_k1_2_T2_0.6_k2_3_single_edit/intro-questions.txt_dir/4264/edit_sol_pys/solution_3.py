

N = int(input())

oddCount = 0
for i in range(1, N + 1):
    if len(str(i)) % 2 == 1:
        oddCount += 1

print(oddCount)
