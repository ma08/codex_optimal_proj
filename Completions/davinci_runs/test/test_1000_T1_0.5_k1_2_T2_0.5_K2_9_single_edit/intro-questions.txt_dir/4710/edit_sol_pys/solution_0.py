

def main():
    a, b = map(int, input().split())
    print(a * b if a < 10 and b < 10 else -1)


if __name__ == '__main__':
    main()
