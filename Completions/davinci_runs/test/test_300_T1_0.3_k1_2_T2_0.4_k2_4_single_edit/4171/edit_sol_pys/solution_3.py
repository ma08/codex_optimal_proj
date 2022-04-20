

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(max(0, a[-1] - a[0] - k))

if __name__ == '__main__':
    main()
