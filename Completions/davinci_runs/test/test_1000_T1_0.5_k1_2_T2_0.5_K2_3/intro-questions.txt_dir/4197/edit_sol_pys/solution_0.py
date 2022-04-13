
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(*a, sep='\n')


if __name__ == '__main__':
    main()
