

N, M, H = map(int, input().split())

for i in range(N):
    match = int(input())**2
    if match <= N*M or match <= H*H or match <= (N**2 + H**2)**0.5:
        print("DA")
    else:
        print("NE")
