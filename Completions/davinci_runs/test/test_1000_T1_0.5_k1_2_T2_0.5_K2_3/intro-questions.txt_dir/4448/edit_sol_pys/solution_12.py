

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        print(a[i] + b[i], end=' ')

if __name__ == '__main__':
    main()
