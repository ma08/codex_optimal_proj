

def main():
    x1, y1, x2, y2 = map(int, input().split())  # Вводим координаты первого прямоугольника
    x3, y3, x4, y4 = map(int, input().split())  # Вводим координаты второго прямоугольника
    x5, y5, x6, y6 = map(int, input().split())  # Вводим координаты третьего прямоугольника

    if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3:  # Проверка на пересечение с вторым прямоугольником
        if x1 >= x6 or x2 <= x5 or y1 >= y6 or y2 <= y5:  # Проверка на пересечение с третьим прямоугольником
            print("YES")  # Пересекаются
        else:
            print("NO")  # Не пересекаются
    else:
        print("NO")  # Не пересекаются

if __name__ == "__main__":
    main()
