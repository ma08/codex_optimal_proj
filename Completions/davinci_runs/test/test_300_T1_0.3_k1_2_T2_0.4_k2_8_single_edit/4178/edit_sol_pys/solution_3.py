

n = int(input())
h = list(map(int, input().split()))
flag = True
for i in range(n-1):
    if h[i] > h[i+1]:
        h[i+1] += 1
        if h[i] > h[i+1]:
            flag = False

if flag:
    print("Yes")
else:
    print("No")
