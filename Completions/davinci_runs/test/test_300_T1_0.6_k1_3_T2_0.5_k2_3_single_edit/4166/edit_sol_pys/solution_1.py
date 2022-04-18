

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        s, c = map(int, input().split())
        if a[i] != 0 and (a[i] < 0 or a[i] > 9):
            print(-1)
            return
        a[s-1] = c
            if a[i] != 0 and a[i] == 0:
                print(-1)
                return
    for i in range(n):
        if i == 0 and a[i] == 0:
            print(-1)
            return
        elif i == 0 and a[i] != 0:
        elif i == 1 and a[0] == 0 and a[i] == 0:
            print(-1)
            return
        elif i == 1 and a[0] == 0 and a[i] != 0:
            print(a[i], end="")
            print(a[i], end="")
            if a[i] != 0 and a[i] == 0:
                print(-1)
                return
        else:
            print(a[i], end="")
    print("")

if __name__ == '__main__':
    main()
