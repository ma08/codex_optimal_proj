

def main():
    n = int(input())
    a = list(input())
    f = list(map(int, input().split()))
    f = [0] + f + [0]

    for i in range(n+1):
        if f[i] > f[i+1]:
            a[i] = '('
        elif f[i] < f[i+1]:
            a[i] = ')'
        else:
            a[i] = '_'

    a = ''.join(a).replace('_', '')

    print(a)

if __name__ == '__main__':
    main()
