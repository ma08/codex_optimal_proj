

def main():
    n = int(input())
    t = input()
    s = [' ']*n
    for i in range(n, 0, -1):
        if n%i == 0:
            for j in range(i):
                s[j::i] = list(t[j::i])[::-1]
            t = ''.join(s)
    print(t)

if __name__ == "__main__":
    main()
