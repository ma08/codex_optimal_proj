

def main():
    s = input()
    n = len(s)
    for i in range(n // 2, -1, -1):
        if s[n - i - 1:n] == s[n - i * 2 - 1:n - i - 1]:
            print(n - i)
            break

if __name__ == '__main__':
    main()
