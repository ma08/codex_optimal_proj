

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(m):
        s, c = map(int, input().split())
        a[s-1] = c
    for i in range(n):
        if i == 0 and a[i] == 0 and n != 1:
            a[i] = 1
        print(a[i], end="")
    print("")

if __name__ == '__main__':
    main()
