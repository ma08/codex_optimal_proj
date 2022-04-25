

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    for i in range(10):
        a = a.replace(str(i), ''.join(['0']*f[i]))

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
