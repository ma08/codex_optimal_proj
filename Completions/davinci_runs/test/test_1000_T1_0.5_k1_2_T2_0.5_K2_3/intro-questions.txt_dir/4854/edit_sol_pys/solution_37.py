n, c = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (c + 1)
for i in range(n):
    freq[arr[i]] += 1

for i in range(c + 1):
    if freq[i] > 0:
        print((str(i) + ' ') * freq[i], end='')
