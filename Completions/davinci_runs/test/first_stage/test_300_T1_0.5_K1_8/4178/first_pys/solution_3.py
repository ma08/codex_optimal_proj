

from sys import stdin

n = int(stdin.readline())
h = list(map(int,stdin.readline().split()))

for i in range(1,n):
    if h[i-1] > h[i]:
        h[i] += 1
        if h[i-1] > h[i]:
            print("No")
            exit()

print("Yes")