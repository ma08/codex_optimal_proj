

def main():
    n = int(input())
    a = input().split()
    b = input().split()
    c = input().split()
    d = input().split()
    for i in range(n):
        if a[i] == b[i] == c[i] == d[i]:
            print('YES')
            return
    print('NO')


if __name__ == "__main__":
    main()
