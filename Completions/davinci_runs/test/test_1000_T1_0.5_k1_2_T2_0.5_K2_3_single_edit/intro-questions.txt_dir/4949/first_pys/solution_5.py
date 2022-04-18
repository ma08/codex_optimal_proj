
N, W, H = [int(x) for x in input().split()]
box = W * H

for _ in range(N):
    match = int(input())
    if match ** 2 <= box:
        print("DA")
    else:
        print("NE")