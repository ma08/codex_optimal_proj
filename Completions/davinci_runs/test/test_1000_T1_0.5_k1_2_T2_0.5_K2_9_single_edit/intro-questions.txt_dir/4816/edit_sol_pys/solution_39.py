


def main():
    x, y = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    print(min(min(y - y1, y2 - y), min(x - x1, x2 - x)) * 2)


if __name__ == "__main__":
    main()
