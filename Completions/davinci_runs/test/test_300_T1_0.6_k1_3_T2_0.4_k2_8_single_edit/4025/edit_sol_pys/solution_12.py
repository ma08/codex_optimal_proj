
def main():
    a, b, c = map(int, input().split())

    if a + b + c > 7:
        print(7)

    else:
        print(a + b + c)

if __name__ == '__main__':
    main()
