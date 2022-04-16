

def main():
    a = int(input())
    b, c = map(int, input().split())
    s = str(input())
    print('{} {}'.format(a + b + c, s))


if __name__ == '__main__':
    main()
