

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    c = 0
    for i in range(n):
        c += a[i]
    print(c)

if __name__ == '__main__':
    main()
