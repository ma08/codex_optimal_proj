
n = int(input())

count = 0
for i in range(1, n+1):
    count += len(str(i)) % 2

print(count)
