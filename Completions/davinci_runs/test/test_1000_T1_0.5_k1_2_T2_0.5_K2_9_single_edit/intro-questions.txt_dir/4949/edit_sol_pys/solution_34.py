
N, W, H = map(int, input().split())

for _ in range(N):
    match_number = int(input())
    if match_number <= (W**2 + H**2)**0.5:
        print("DA")
    else:
        print("NE")
