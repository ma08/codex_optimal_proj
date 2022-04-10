

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a == 1:
        print(a + b)
    else:
        print(2 * (a + b - 2))

if __name__ == '__main__':
    main()