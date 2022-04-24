

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a.sort()
    print(a[0])
    print(a[-1])

if __name__ == '__main__':
    main()
