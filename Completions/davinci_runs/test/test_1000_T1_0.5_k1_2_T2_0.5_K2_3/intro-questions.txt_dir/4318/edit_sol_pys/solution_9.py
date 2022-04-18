def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    print(s.index(s[0]) + 1)


if __name__ == '__main__':
    main()
