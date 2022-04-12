
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[0] - a[-1])


if __name__ == '__main__':
    main()
