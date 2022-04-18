def main():
    x, y, x1, y1, x2, y2 = map(int, input().split())  # list(map(int, input().split()))
    print(min(min(y - y1, y2 - y), min(x - x1, x2 - x)))  # min(y - y1, y2 - y, x - x1, x2 - x)


if __name__ == "__main__":
    main()
