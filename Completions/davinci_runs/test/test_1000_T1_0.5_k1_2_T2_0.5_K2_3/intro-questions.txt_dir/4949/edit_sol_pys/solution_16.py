N, W, H = [int(x) for x in input().split()]
box = W * H

for _ in range(N):
    match_stick = int(input())
    if match_stick ** 2 <= box:
        print("YES")
    else:
        print("NO")
