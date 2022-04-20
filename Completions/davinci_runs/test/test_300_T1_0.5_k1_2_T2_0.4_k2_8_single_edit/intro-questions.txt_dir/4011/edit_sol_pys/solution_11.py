

def main():
    n = int(input())
    a = input()
    f = map(int, input().split())
    f = [0] + list(f)

    for i in range(n):
        a[i] = f[int(a[i])]

    print(''.join(a))

if __name__ == '__main__':
    main()
