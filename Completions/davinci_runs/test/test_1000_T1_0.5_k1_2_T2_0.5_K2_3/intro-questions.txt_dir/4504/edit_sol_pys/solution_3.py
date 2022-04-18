
def main():
    s = input()
    n = len(s)
    for i in range(n//2+1, 0, -1):
        if s[n-i:n] == s[n-i * 2:n - i]:
            print(i)
            break


if __name__ == '__main__':
    main()
