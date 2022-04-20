

def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if a == 1:
        print(4 * a + 4 * b)
    else:
        print(4 * a + 2 * b)

if __name__ == '__main__':
    main()