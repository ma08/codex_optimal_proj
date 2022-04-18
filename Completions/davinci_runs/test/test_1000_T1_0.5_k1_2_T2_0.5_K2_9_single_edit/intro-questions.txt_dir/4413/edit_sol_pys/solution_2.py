def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n):
        print(a[i]+b[i], end=' ')




if __name__ == '__main__':
    main()
