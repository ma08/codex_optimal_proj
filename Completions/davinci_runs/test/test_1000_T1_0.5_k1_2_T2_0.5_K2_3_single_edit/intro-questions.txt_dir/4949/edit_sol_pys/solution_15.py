

N, W, H = map(int, input().split()) # 3

for _ in range(N):
    match = int(input()) # 4
    if match <= (W**2 + H**2)**0.5:
        print("DA") # DA
    else:
        print("NE")
