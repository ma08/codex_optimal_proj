


def main():
    n = int(input())
    t = input()
    s = ['']*n
    for i in range(n, 1, -1):
        if n%i == 0:
            s[::i] = t[::i][::-1]
            t = ''.join(s)
    print(s)

if __name__ == '__main__':
    main()
