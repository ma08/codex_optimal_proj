
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1] - a[0] - 1)

if __name__ == '__main__':
    main()
