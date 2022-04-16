

def main():
    x, y = map(int, input().split())

    if y % 2 == 0 and x * 2 <= y and y <= x * 4:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
