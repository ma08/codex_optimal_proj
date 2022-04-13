
def main():
    x, y, x1, y1, x2, y2 = map(int, input().split())
    print(max(min(y - y1, y2 - y), min(x - x1, x2 - x)))


if __name__ == "__main__":
    main()
