
def main():
    a, b = map(int, input().split())
    if a <= 4 <= b:
        print('Yes')
    elif a <= 8 <= b:
        print('Yes')
    elif a <= 12 <= b:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
