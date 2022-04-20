

A, B = map(int, input().split())

ans = A * B

if ans <= 9:
    print(ans)
else:
    print(-1)