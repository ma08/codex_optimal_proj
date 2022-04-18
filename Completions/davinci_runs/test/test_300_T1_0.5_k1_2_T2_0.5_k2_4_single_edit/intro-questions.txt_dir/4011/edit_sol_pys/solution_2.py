

def solve(n, a, f):
    for i in range(n):
        a[i] = f[int(a[i])]

    return ''.join(a)

def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f = [0] + f

    a = solve(n, a, f)

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
