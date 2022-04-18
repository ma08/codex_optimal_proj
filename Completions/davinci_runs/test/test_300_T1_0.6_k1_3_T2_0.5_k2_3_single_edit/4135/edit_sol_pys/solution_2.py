
def main():
    n = int(input())
    t = input()
    s = list(t)
    for i in range(n-1, 0, -1):
        if n % i == 0:
            for j in range(i):
                s[j::i] = t[j::i][i-1::-1]
            t = ''.join(s)
    print(t)

if __name__ == '__main__':
    main()
