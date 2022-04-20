

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        s, c = map(int, input().split())
        if a[s-1] != 0 and a[s-1] != c:
            print(-1)
            return
        else:
            a[s-1] = c
    for i in range(n):
        if i == 0:
            if a[i] == 0:
                print(1, end="")
            else:
                print(a[i], end="")
        else:
            if a[i] == 0:
                print(0, end="")
            else:
                print(a[i], end="")
    print("")

if __name__ == '__main__':
    main()
