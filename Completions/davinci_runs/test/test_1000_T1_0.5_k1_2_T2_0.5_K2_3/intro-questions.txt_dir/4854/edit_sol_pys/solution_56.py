n, c = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (c + 1)
for i in range(n):
    freq[arr[i]] += 1

for i in range(1, c + 1):
    print((str(i) + ' ') * freq[i], end='')
