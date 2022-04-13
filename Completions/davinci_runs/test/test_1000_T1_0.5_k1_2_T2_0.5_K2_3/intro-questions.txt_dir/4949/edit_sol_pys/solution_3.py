#
N, W, H = (int(x) for x in input().split())
box = W * H  # box size

for _ in range(N):
    match_size = int(input())
    if match_size ** 2 <= box:
        print("DA")
    else:
        print("NE")
