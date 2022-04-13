


def main():
    x, y, x1, y1, x2, y2 = map(float, input().split())
    print(min(x - x1, x2 - x, y - y1, y2 - y, (x1 - x) ** 2 + (y1 - y) ** 2,
              (x1 - x) ** 2 + (y2 - y) ** 2, (x2 - x) ** 2 + (y1 - y) ** 2,
              (x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5)



if __name__ == "__main__":
    main()
