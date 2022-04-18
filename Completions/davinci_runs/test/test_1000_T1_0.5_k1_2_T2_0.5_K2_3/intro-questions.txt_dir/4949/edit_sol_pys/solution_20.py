
N, W, H = map(int, input().split())

for i in range(N):
    match = float(input())
    if match <= W or match <= H or match <= (W**2 + H**2)**0.5:  # корень из суммы квадратов длины и ширины
        print("DA")
    else:
        print("NE")
