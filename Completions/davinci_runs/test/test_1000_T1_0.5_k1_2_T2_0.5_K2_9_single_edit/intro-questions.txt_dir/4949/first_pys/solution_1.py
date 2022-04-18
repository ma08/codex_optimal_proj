

N, W, H = map(int, input().split())
for i in range(N):
    if int(input()) <= max(W, H):
        print("DA")
    else:
        print("NE")