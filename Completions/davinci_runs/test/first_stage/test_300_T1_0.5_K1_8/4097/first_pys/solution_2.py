

n = int(input())
b = list(map(int, input().split()))

if b[1] - b[0] == b[2] - b[1]:
    print(0)
elif b[1] - b[0] < b[2] - b[1]:
    if b[0] + b[2] - b[1] <= 0:
        print(-1)
    else:
        print(1)
else:
    if b[0] + b[1] - b[2] <= 0:
        print(-1)
    else:
        print(1)