

def main():
    n = int(input())
    a = list(input())  # list of numbers
    f = list(map(int, input().split()))  # list of frequencies
    f = [0] + f  # add 0 to the beginning

    for i in range(n):
        a[i] = f[int(a[i])]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
