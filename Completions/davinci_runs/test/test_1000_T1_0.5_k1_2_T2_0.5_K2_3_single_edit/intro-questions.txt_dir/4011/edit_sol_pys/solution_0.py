

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    for i in range(n):
        a[i] = f[int(a[i])]

    a = ''.join(str(a))

    print(a)

if __name__ == '__main__':
    main()
