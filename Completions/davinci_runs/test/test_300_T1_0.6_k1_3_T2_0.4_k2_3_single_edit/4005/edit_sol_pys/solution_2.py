

def main():
    x1, y1, x2, y2 = [int(i) for i in input().split()]  # координаты первого прямоугольника
    x3, y3, x4, y4 = [int(i) for i in input().split()]  # координаты второго прямоугольника
    x5, y5, x6, y6 = [int(i) for i in input().split()]  # координаты третьего прямоугольника
    if (x1 >= x4 or x3 >= x2 or y1 >= y4 or y3 >= y2):  # проверка пересечения первого и второго прямоугольника
        print("NO")
        return
    if (x1 >= x6 or x5 >= x2 or y1 >= y6 or y5 >= y2):  # проверка пересечения первого и третьего прямоугольника
        print("NO")
        return
    print("YES")

if __name__ == "__main__":
    main()
