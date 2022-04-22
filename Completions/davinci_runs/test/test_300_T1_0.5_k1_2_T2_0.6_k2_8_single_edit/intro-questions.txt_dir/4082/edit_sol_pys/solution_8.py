

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split())) + [0]
    b = list(map(int, input().split()))
    c = [0] * (n + 1)
    for i in range(n):
        c[i+1] = c[i] + a[i]
    for i in range(m):
        l, r = map(int, input().split())
        print(c[r] - c[l-1])

if __name__ == '__main__':
    main()
