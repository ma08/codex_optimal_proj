

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))
    f = [0] + f

    b = ''
    for i in a:
        b += str(f[int(i)])

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
