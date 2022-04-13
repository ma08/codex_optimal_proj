
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for i in range(m):
        for j in range(n):
            if a[j] <= b[i] and b[i] <= c[j]:
                print(j + 1)

if __name__ == '__main__':
    main()
