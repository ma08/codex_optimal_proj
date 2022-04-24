def reverse(t, i):
    n = len(t)
    s = ['']*n
    for j in range(i):
        s[j::i] = t[j::i][::-1]
    return ''.join(s)


def main():
    n = int(input())
    t = input()
    for i in range(n, 0, -1):
        if n%i == 0:
            t = reverse(t, i)
    print(t)

if __name__ == '__main__':
    main()
