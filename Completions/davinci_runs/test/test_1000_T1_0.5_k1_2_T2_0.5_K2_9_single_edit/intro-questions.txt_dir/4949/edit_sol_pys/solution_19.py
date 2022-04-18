N, W, H = [int(x) for x in input().split()]
box = W * H

for _ in range(N):
    match = int(input()) ** 2
    if match <= box:
        print("DA")
    else:
        print("NE")
