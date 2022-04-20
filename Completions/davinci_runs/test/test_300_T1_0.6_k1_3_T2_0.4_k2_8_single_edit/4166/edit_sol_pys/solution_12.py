

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        s, c = map(int, input().split())
        a[s - 1] = c
    for i in range(n):
        if i == 0 and a[i] == 0 and n != 1:
            print(-1)
            return
        elif i == 0 and a[i] != 0 and n != 1:
        elif i == 0 and a[i] == 0 and n == 1:
            print(0)
            return
        elif i == 0 and a[i] != 0 and n == 1:
            print(a[i])
            return
            print(a[i], end="")
        else:
            print(a[i], end="")
    print("")

if __name__ == '__main__':
    main()
