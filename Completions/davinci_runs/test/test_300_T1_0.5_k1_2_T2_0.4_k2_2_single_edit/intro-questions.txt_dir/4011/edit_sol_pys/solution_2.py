

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    for i in a:
        print(f[int(i)], end='')

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
