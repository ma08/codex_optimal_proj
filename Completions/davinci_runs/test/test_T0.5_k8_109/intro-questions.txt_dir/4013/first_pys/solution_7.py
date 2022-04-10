

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(min(a[n-2] - a[0], a[n-1] - a[1]))

if __name__ == '__main__':
    main()