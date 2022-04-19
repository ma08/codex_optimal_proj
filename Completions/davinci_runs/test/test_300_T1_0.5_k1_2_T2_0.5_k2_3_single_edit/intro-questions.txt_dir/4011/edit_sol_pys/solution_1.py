

def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f = [0] + f

    for i in range(n-1):
        a[i+1] = f[int(a[i+1])]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
