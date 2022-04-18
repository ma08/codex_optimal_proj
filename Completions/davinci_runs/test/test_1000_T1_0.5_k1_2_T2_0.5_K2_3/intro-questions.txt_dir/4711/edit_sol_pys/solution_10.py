
def main():
    a, b, c, d = map(int, input().split())
    print(min(a + b, a + c, b + c, d))


if __name__ == '__main__':
    main()
