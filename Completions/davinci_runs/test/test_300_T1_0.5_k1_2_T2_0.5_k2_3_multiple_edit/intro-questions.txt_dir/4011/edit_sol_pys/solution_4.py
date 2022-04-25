
def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    for i in range(n):
        print(f[int(a[i])], end='')

    print()

if __name__ == '__main__':
    main()
