
def main():
    n = int(input())
    a = list(input())
    p = list(map(int, input().split()))
    p = [0] + p + [0]

    for i in range(n):
        a[i] = p[int(a[i])]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
