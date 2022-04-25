n = int(input())
a = list(map(int, input().split()))

disturbing = []

for i in range(1, n):
    if a[i - 1] == 1 and a[i + 1] == 1 and a[i] == 0:
        disturbing.append(i)

print(len(disturbing))
