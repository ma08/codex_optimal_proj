

def main():
    swathers, stages = [int(x) for x in input().split()]  # количество команд и этапов
    times = []
    for i in range(swathers):  # вводим время на каждом этапе
        times.append([int(x) for x in input().split()])
    times = sorted(times)  # сортируем команды по времени на первом этапе
    for i in range(1, len(times)):  # добавляем время на предыдущем этапе к времени на текущем
        for j in range(stages):
            times[i][j] += times[i - 1][j]
    for i in range(swathers):
        print(times[i][stages - 1], end=' ')


main()
