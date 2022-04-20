

def main():
    n, m = map(int, input().split())
    a = [1] * n
    for i in range(m):
        s, c = map(int, input().split())
        a[s-1] = c
    for i in range(n):
        print(a[i], end="")
    print()

if __name__ == '__main__':
    main()
