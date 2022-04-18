
N, W, H = map(int, input().split())
box = W ** 2 + H ** 2

for _ in range(N):
    match = input()
    if int(match) ** 2 <= box:
        print("YES")
    else:
        print("NO")
