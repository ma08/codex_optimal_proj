

def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f = [0] + f + [0]

    for i in range(n):
        a[i] = f[int(a[i])]

    a = ''.join(map(str, a))

    print(a)

if __name__ == '__main__':
    main()
