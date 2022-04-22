

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    a = ''.join([str(f[int(c)]) for c in a])

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
