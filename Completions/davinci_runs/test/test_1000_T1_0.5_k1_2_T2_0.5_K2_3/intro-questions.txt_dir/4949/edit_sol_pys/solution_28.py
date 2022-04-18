n, w, h = map(int, input().split())

for i in range(n):
    match = int(input())
    if match <= w or match <= h or match <= (w**2 + h**2)**0.5:
        print("DA")
    else:
        print("NE")
