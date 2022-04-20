

def main():
    n, m = map(int, input().split())  # Считываем количество отрезков и точек
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())  # Считываем координаты отрезков
        segments.append((l, r))
    segments.sort(key=lambda x: x[0])  # Сортируем отрезки по левой координате
    points = []
    for i in range(n-1):
        if segments[i][1] < segments[i+1][0]:  # Если правая координата отрезка меньше левой координаты следующего отрезка
            points.append(segments[i][1])
    print(len(points))  # Выводим количество точек
    print(*points)  # Выводим точки

if __name__ == "__main__":
    main()
