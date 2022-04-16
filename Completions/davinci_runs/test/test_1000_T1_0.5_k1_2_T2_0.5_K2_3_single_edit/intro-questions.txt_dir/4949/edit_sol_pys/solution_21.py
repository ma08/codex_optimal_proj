

N, W, H = map(int, input().split()) # Считываем данные

for i in range(N):
    match = int(input()) # Считываем длину матча
    if match <= W or match <= H or match <= (W**2 + H**2)**0.5: # Проверяем попадает ли матч в прямоугольник
        print("DA")
    else: # Если нет
        print("NE")
