
def main():
    a, b, c = map(int, input().split())
    print(min(a + b, a + c, b + c))


if __name__ == '__main__':
    main()
