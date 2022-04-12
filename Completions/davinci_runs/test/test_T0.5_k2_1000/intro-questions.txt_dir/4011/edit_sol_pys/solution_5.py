

def main():
    n = int(input())
    a = input().split()
    f = list(map(int, input().split()))

    for i in range(n):
        a[i] = str(f[int(a[i])])

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
