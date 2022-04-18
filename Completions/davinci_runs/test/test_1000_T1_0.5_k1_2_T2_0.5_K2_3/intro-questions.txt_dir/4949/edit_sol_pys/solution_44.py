
N, W, H = map(int, input().split())

for _ in range(N):
    match = int(input())
    if match <= (W * W + H * H)**0.5:
        print("DA") 
    else:
        print("NE")
