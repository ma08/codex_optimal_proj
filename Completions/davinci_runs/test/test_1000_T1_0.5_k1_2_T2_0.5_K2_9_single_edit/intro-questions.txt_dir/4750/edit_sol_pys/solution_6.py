

def main():
    q = int(input())
    for _ in range(q):
        n, m, x, y = map(int, input().split())
        if n == 1:
            print(1)
        elif m == 1:
            print(1)
        elif n == 2:
            if x == 1:
                print(2)
            else:
                print(1)
        elif m == 2:
            if y == 1:
                print(2)
            else:
                print(1)
        elif n > m:
            if n % 2 == 0:
                if x == n:
                    print(n-1)
                else:
                    print(n+1)
            else:
                if x == n:
                    print(n+1)
                else:
                    print(n-1)
        elif n < m:
            if m % 2 == 0:
                if y == m:
                    print(m-1)
                else:
                    print(m+1)
            else:
                if y == m:
                    print(m+1)
                else:
                    print(m-1)

if __name__ == "__main__":
    main()
