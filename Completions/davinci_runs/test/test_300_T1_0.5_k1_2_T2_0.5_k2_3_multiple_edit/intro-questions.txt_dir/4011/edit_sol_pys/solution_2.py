

def main():
    n = int(input())
    a = list(map(int, input().split()))
    f = list(map(int, input().split()))
    f.insert(0, 0)

    for i in range(n):
        a[i] = f[a[i]]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
