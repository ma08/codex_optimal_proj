

# input
def main():
    n = int(input())
    a = list(input())

    # process
    f = list(map(int, input().split()))
    f = [0] + f

    # output
    for i in range(n):
        a[i] = f[int(a[i])]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
