
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a.index(a[0]) + 1)


if __name__ == '__main__':
    main()
