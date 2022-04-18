

N, W, H = map(int, input().split()) # ширина, дължина и височина

for _ in range(N):
    match = int(input())
    if match <= (W**2 + H**2)**0.5: # проверка дали е в квадрата с горните краища на кутията
        print("DA")
    else:
        print("NE")
