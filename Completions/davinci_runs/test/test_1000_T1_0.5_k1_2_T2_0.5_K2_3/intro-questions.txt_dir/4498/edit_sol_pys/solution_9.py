def main():
    a, b, c, d = map(int, input().split())
    if abs(a - b) <= d and abs(b - c) <= d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
