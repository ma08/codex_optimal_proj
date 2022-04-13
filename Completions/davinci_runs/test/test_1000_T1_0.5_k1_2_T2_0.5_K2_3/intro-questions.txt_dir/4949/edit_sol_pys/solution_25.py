N, W, H = (int(x) for x in input().split())
box = W * H

for _ in range(N):
    match_size = int(input())  # diagonal
    if match_size ** 2 <= box:  # diagonal^2 <= box
        print("DA")
    else:
        print("NE")
