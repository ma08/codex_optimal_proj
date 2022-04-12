N, W, H = [int(x) for x in input().split()]
box = W**2 + H**2

for _ in range(N):
    match = int(input())
    if match**2 <= box:
        print("YES")
    else:
        print("NO")
