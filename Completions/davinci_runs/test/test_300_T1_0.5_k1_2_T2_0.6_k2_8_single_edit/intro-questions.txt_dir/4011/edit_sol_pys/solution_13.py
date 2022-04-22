

def main():
    n = int(input())
    a = list(input().split())
    f = list(map(int, input().split()))

    for i in range(n):
        a[i] = f[int(a[i]) - 1]

    a = ' '.join(map(str, a))

    print(a)

if __name__ == '__main__':
    main()
