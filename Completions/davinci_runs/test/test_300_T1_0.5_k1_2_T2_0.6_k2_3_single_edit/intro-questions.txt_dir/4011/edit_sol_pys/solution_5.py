

def main():
    n = int(input())
    a = list(input().strip())
    f = list(map(int, input().split()))
    f = [0] + f

    a = list(map(str, a))
    for i in range(n):
        a[i] = f[int(a[i])]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
