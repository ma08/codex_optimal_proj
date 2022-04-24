


def main():
    n = int(input())
    t = input()
    s = ['']*n
    for i in range(n, 1, -1):
        if n%i == 0:
            for j in range(i):
                s[j::i] = t[j::i][::-1]
            t = ''.join(s) # need to reverse back
    print(s)

if __name__ == '__main__':
    main()
