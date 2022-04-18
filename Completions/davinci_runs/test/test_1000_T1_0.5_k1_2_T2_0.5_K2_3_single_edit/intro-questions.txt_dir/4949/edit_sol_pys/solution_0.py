
N, W, H = map(int, input().split())

for i in range(N):
    match = int(input())
    if match <= W or match <= H or match <= (W * W + H * H) ** 0.5:
        print("DA")
    else:
        print("NE")
