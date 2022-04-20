

n,x = map(int,input().split())
l = list(map(int,input().split()))

count = 0
for i in range(n):
    if x - l[i] >= 0:
        count += 1
        x -= l[i]
    else:
        break

print(count)