def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i[0] for i in sorted(enumerate(a, 1), key=lambda x: x[1])]
    print(*a, sep='\n')


if __name__ == '__main__':
    main()
