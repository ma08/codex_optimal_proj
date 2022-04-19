

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k, n):
        print(a[i], end=' ')
    for i in range(k):
        print(a[i], end=' ')

if __name__ == '__main__':
    main()
