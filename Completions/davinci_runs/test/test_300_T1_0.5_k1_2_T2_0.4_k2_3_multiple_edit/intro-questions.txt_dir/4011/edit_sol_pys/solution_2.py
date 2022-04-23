
def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    a = ''.join([str(f[int(a[i])]) for i in range(n)])

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
