

def main():
    n = int(input())
    s = list(input())
    f = list(map(int, input().split()))
    f = [0] + f

    for i in range(n):
        s[i] = f[int(s[i])]

    s = ''.join(s)

    print(s)

if __name__ == '__main__':
    main()
