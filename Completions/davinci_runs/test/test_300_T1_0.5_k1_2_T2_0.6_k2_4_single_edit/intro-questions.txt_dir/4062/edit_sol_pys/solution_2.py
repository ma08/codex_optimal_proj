

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(min(a[-1] - a[0], abs(a[-1] - a[1]), abs(a[-2] - a[0])))

if __name__ == '__main__':
    main()
