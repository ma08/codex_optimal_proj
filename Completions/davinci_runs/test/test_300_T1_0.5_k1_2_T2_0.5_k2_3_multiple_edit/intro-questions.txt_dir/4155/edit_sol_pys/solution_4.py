N = int(input())
H = list(map(int,input().split()))

count = 0
for i in range(N):
    if H[i] > count:
        count = H[i]
print(count)
