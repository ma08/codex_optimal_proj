
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[-1]:
        print(0)
    else:
        print(a[-1] - a[0] - 1)

if __name__ == '__main__':
    main()
