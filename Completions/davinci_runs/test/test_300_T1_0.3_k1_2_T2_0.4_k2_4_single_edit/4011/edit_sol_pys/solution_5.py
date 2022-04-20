

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    a = list(map(int, list(a)))
    for i in range(n):
        a[i] = f[a[i]]
    print(''.join(map(str, a)))

if __name__ == '__main__':
    main()
